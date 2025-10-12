#!/usr/bin/env python3
"""
Simple OCR Demo for Historical Documents
=======================================

This script demonstrates how to use Tesseract OCR on selected pages (cover and poem) 
converted from a PDF using ImageMagick.

Key features:
<<<<<<< HEAD
- Extracts only specified pages (cover page and a poem pages)
=======
- Extracts only specified pages (cover page and a poem page)
>>>>>>> 09e7db2b6784cf2f5ec731099e13497e364e28cc
- Simple OCR with PSM 3 (default mode)
- Text cleaning and formatting
- Results saved to text files

Usage:
    python simple_ocr.py "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/images/TheColoredAmerican.pdf"
"""

import sys
from pathlib import Path
from wand.image import Image
import pytesseract
from PIL import Image as PILImage

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = {
        'wand': 'wand',
        'pytesseract': 'pytesseract',
        'PIL': 'Pillow'
    }
    for package, install_name in required_packages.items():
        try:
            __import__(package)
        except ImportError:
            print(f"Error: {package} is not installed. Install it using 'pip install {install_name}'.")
            sys.exit(1)

def convert_selected_pages_to_images(pdf_path, output_dir, pages_to_extract):
    """
    Convert only specified pages of a PDF into images.
    pages_to_extract: list of 1-based page numbers to extract (e.g., [1, 9, 10])
    """
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Converting pages {pages_to_extract} of {pdf_path} to images...")
    try:
        with Image(filename=str(pdf_path), resolution=300) as pdf:
            for page_num in pages_to_extract:
                idx = page_num - 1  # Wand uses 0-based indexing
                if idx < len(pdf.sequence):
                    with Image(pdf.sequence[idx]) as img:
                        img.format = 'png'
                        image_path = output_dir / f"page_{page_num}.png"
                        img.save(filename=str(image_path))
                        print(f"Saved: {image_path}")
                else:
                    print(f"Warning: Page {page_num} does not exist in PDF.")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        sys.exit(1)

def perform_ocr_on_selected_images(image_dir, output_dir, pages_to_ocr):
    """
    Perform OCR only on specified images and save results to separate text files.
    Saves results as cover_page.txt and truth_poem.txt (combined OCR from pages 9 and 10).
    """
    image_dir = Path(image_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Cover page (page 1)
    cover_file = output_dir / "cover_page.txt"
    page1_image = image_dir / "page_1.png"
    if page1_image.exists():
        print(f"Processing OCR for {page1_image} (cover)...")
        try:
            text = pytesseract.image_to_string(PILImage.open(page1_image))
            with open(cover_file, "w") as f:
                f.write(text)
            print(f"OCR result saved to {cover_file}")
        except Exception as e:
            print(f"Error processing OCR for {page1_image}: {e}")
    else:
        print(f"Warning: {page1_image} does not exist, skipping cover page.")

    # Poem pages (pages 9 and 10)
    poem_file = output_dir / "truth_poem.txt"
    with open(poem_file, "w") as f:
        for page_num in [9, 10]:
            image_file = image_dir / f"page_{page_num}.png"
            if image_file.exists():
                print(f"Processing OCR for {image_file} (poem)...")
                try:
                    text = pytesseract.image_to_string(PILImage.open(image_file))
                    f.write(f"--- Text from page {page_num} ---\n")
                    f.write(text + "\n")
                except Exception as e:
                    print(f"Error processing OCR for {image_file}: {e}")
            else:
                print(f"Warning: {image_file} does not exist, skipping.")
    print(f"OCR result for poem saved to {poem_file}")

if __name__ == "__main__":
    check_dependencies()

    if len(sys.argv) != 2:
        print("Usage: python simple_ocr.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not Path(pdf_path).is_file():
        print(f"Error: The file '{pdf_path}' does not exist.")
        sys.exit(1)

    image_output_dir = "processed-imgs"
    ocr_output_dir = "ocr-pages"
    pages_to_extract = [1, 9, 10]  # Cover page and poem pages

    convert_selected_pages_to_images(pdf_path, image_output_dir, pages_to_extract)
    perform_ocr_on_selected_images(image_output_dir, ocr_output_dir, pages_to_extract) 
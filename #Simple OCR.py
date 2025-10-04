#!/usr/bin/env python3
"""
Simple OCR Script
=================
Usage:
    python simple_ocr.py /Users/indiralessington/Desktop/TheColoredAmerican.pdf
"""

import sys
from pathlib import Path
from wand.image import Image
import pytesseract
from PIL import Image as PILImage

def convert_pdf_to_images(pdf_path, output_dir):
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Converting {pdf_path} to images...")
    try:
        with Image(filename=str(pdf_path), resolution=300) as pdf:
            for i, page in enumerate(pdf.sequence):
                with Image(page) as img:
                    img.format = 'png'
                    image_path = output_dir / f"page_{i + 1}.png"
                    img.save(filename=str(image_path))
                    print(f"Saved: {image_path}")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        sys.exit(1)

def perform_ocr_on_images(image_dir, output_file):
    image_dir = Path(image_dir)
    output_file = Path(output_file)

    print(f"Running OCR on images in {image_dir}...")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for image_file in sorted(image_dir.glob("*.png")):
                print(f"Processing {image_file}...")
                text = pytesseract.image_to_string(PILImage.open(image_file))
                f.write(f"--- Text from {image_file.name} ---\n")
                f.write(text + "\n")
        print(f"OCR results saved to {output_file}")
    except Exception as e:
        print(f"Error performing OCR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simple_ocr.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    image_output_dir = "processed-imgs"
    ocr_output_file = "ocr-results.txt"

    if not Path(pdf_path).exists():
        print(f"PDF file not found: {pdf_path}")
        sys.exit(1)

    convert_pdf_to_images(pdf_path, image_output_dir)
    perform_ocr_on_images(image_output_dir, ocr_output_file)
# OCR-and-AI-Transcription-Project-8510

# Project Overview:

This repository provides tools and instructions for processing an issue of The Colored American Magazine. The second Python script, "Contrast and Enhancement," will examine the cover page. Using OpenAI's GPT-5-nano, I will further process the extracted text from the cover page to interpret or clarify content where OCR is imperfect. 

In my "ocr_pages" folder, I store the text files from experimenting with Tesseract and the text from the cover page. In my "ocr_results" folder, I store the text file results from the cover page, with AI correction and without AI correction.

_________________________________________________________________________________________________________________________________________________________________________________________

## Quick Start

Follow these steps to extract the cover page (page 1) and the poem "Truth" (page 9) using the OCR script:

### 1. Prepare Your Virtual Environment in VSC:
		python -m venv .venv
		source .venv/bin/activate

- **Install system dependencies:**
  - [ImageMagick](https://imagemagick.org/script/download.php)
  - [Tesseract OCR](https://tesseract-ocr.github.io/)
- **Install Python packages:**
  ```python
  pip install wand pytesseract Pillow
  ```
_________________________________________________________________________________________________________________________________________________________________________________________
### 2. Download Your PDF:

- Download an issue of "The Colored American Magazine" as a PDF.
- Note the full path to your PDF file.  
  Example:  
  `/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/images/TheColoredAmerican.pdf`

_________________________________________________________________________________________________________________________________________________________________________________________
### 3. Run the Script

- Open a Python terminal and change directory to where `simple_ocr.py` is located.
- Run the following command (replace the PDF path with your own if different):

  ```python
  python simple_ocr.py "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/images/TheColoredAmerican.pdf"
  ```
_________________________________________________________________________________________________________________________________________________________________________________________
### 4. Extraction Details

- The script automatically extracts:
  - **Cover page:** Only page 1 of the PDF, saving OCR text to `ocr-pages/cover_page.txt`.
  - **Poem "Truth":** Pages 9 and 10 of the PDF, saving combined OCR text to `ocr-pages/truth_poem.txt`.

- Processed page images are saved in the `processed-imgs` directory.

_________________________________________________________________________________________________________________________________________________________________________________________
### 5. Find the Results

- Find your extracted text files in the `ocr-pages` directory:
  - `cover_page.txt` contains the OCR output of the cover page.
  - `truth_poem.txt` contains the OCR output of the poem "Truth" (from pages 9 and 10).


_________________________________________________________________________________________________________________________________________________________________________________________
### 6. Troubleshooting

- If you see errors about missing packages, rerun:
  ```bash
  pip install wand pytesseract Pillow
  ```
- If you see errors about ImageMagick or Tesseract, ensure they are installed and added to your system PATH.
- Make sure you provide the correct path to your PDF file



_________________________________________________________________________________________________________________________________________________________________________________________
To Run Contrast and Enhancement Script "opencv-python" must be installed. Instructions below:

	    pip install opencv-python

If you need `matplotlib numpy` installation instructions, they are below:

		pip install matplotlib numpy

To Run Contrast and Enhancement Script input in Terminal:

		python "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/Contrast and Enhancement.py" --image "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/processed-imgs/page_1.png"

_________________________________________________________________________________________________________________________________________________________________________________________




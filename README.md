# OCR-and-AI-Transcription-Project-8510

# Project Overview:

This repository provides tools and instructions for processing an issue of The Colored American Magazine, a historic Black publication advocating for Black identity and representation in the early 19th century. The second Python script, "Contrast and Enhancement," will examine the cover of The Colored American Magazine. Using OpenAI's GPT-5-nano, I will further process the extracted text to interpret or clarify content where OCR is imperfect. 

_________________________________________________________________________________________________________________________________________________________________________________________

## Quick Start

Follow these steps to run the OCR script on an issue of "The Colored American Magazine":

### 1. Prepare Your Environment

- **Install system dependencies:**
  - [ImageMagick](https://imagemagick.org/script/download.php)
  - [Tesseract OCR](https://tesseract-ocr.github.io/)
- **Install Python packages:**
  ```Python
  pip install wand pytesseract Pillow
  ```
  
### 2. Download Your PDF

- Download an issue of "The Colored American Magazine" as a PDF.
- Note the full path to your PDF file.  
  Example:  
  `/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/images/TheColoredAmerican.pdf`

### 3. Run the Script

- Open a terminal and change directory to where `simple_ocr.py` is located.
- Run the following command (replace the PDF path with your own if different):

  ```python
  python simple_ocr.py "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/images/TheColoredAmerican.pdf"
  ```

  Or, if you need to use the full path to your Python interpreter:

  ```python
  "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/ocr_proj_env/bin/python" "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/simple_ocr.py" "/Users/indiralessington/Desktop/8510 Unit 2 Converting Hist. Docs. Text to Digital Data/images/TheColoredAmerican.pdf"
  ```

### 4. Find the Results

- The script will:
  - Create a folder called `processed-imgs` containing PNG images for each PDF page.
  - Save all extracted text to `ocr-results.txt`.
  - Attempt to extract the poem "Truth" and save it to `poem_truth.txt`.

### 5. Troubleshooting

- If you see errors about missing packages, rerun:
  ```bash
  pip install wand pytesseract Pillow
  ```
- If you see errors about ImageMagick or Tesseract, ensure they are installed and added to your system PATH.
- Make sure you provide the correct path to your PDF file.























_________________________________________________________________________________________________________________________________________________________________________________________
To Run Contrast and Enhancement Script "opencv-python" must be installed. Instructions below:

	    pip install opencv-python





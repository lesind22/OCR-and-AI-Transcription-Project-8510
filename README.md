# OCR-and-AI-Transcription-Project-8510

# Project Overview:

This repository provides tools and instructions for processing issues of "The Colored American Magazine," a historic Black publication advocating for Black identity and representation in the early 19th century.

_________________________________________________________________________________________________________________________________________________________________________________________


# Workflow Instructions:

- Select one issue of "The Colored American Magazine" and download it as a PDF
- Run the provided Python script to:
  - Convert the PDF into images (using ImageMagick via wand).
  - Perform OCR on the images to extract text (using Tesseract).
  - Save results to a text file.

- The script extracts all text
- To focus on the cover page and the poem entitled "Truth,"
	- Review the output file (`ocr-results.txt`) and locate these sections manually 

- To further process the extracted text with OpenAI’s GPT-5-nano to interpret or clarify content, especially where OCR is imperfect

_________________________________________________________________________________________________________________________________________________________________________________________

# Goal of Project:
- Analyze how GPT-5-nano handles text with imperfect OCR:
	 - Observe if the model helps clarify content.  
  	 - Note where it may distort images or omit language.

_________________________________________________________________________________________________________________________________________________________________________________________

# Requirements and Installation of Pytesseract:
- Python 3.x
- [ImageMagick](https://imagemagick.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) 
- Python packages and How to Install: `wand`, `pytesseract`, `Pillow`
    ```bash
    pip install wand pytesseract Pillow
    ```

_________________________________________________________________________________________________________________________________________________________________________________________

# Usage:

1. Place your selected PDF in the `input/` directory.

2. Run the following command to convert the PDF to images:
    ```bash
    magick input/yourfile.pdf input/page_%d.png
    ```
    
3. Run Tesseract on each image to extract text:
    ```bash
    tesseract input/page_1.png output/page_1.txt
    ```
    
4. Run the provided "simple_ocr" Python script to:
    - Extract the cover page
    - Extract the poem “Truth”
    - Prepare text for GPT-5-nano interpretation

5. Review results in the `output/` directory.

_________________________________________________________________________________________________________________________________________________________________________________________

# Instructions for Creating A Virtual Environment:
_________________________________________________________________________________________________________________________________________________________________________________________

Before installing pdf2image, create a virtual environment in your VSCode terminal. Instructions below:
   
   		 python3 -m venv venv
    	 source .venv/bin/activate

_________________________________________________________________________________________________________________________________________________________________________________________
To Run Contrast and Enhancement Script "opencv-python" must be installed. Instructions below:

	    pip install opencv-python





# OCR-and-AI-Transcription-Project-8510

# Project Overview:

This repository provides tools and instructions for processing issues of "The Colored American Magazine," a historic Black publication advocating for Black identity and representation in the early 19th century.

_________________________________________________________________________________________________________________________________________________________________________________________


# Workflow Instructions:

- Select one issue of "The Colored American Magazine" and download it as a PDF
- Convert the PDF to images using ImageMagick
- Run the images through Tesseract to perform Optical Character Recognition (OCR)
- Extract the cover page and the poem entitled "Truth" from the publication
- Use OpenAI’s GPT-5-nano to process and interpret the extracted text

_________________________________________________________________________________________________________________________________________________________________________________________

# Goal of Project:
- Analyze how GPT-5-nano handles text with imperfect OCR:  
  - Observe if the model helps clarify content.  
  - Note where it may distort images or omit language.

_________________________________________________________________________________________________________________________________________________________________________________________

# Requirements:
- Python 3.0 (most recent version available) 
- ImageMagick
- Tesseract
- OpenAI GPT-5-nano API access

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

# Instructions for Installation of Packages:
_________________________________________________________________________________________________________________________________________________________________________________________


Before installing pdf2image, create a virtual environment in your VSCode terminal. Instructions below:
   
    python3 -m venv venv
    source .venv/bin/activate

_________________________________________________________________________________________________________________________________________________________________________________________

To install Wand via Python in VSCode Terminal (if necessary):

		pip install wand



To install ImageMagick via VSCode Terminal:

		pip install imagemagick
		
_________________________________________________________________________________________________________________________________________________________________________________________

To Run Contrast and Enhancement Script "opencv-python" must be installed. Instructions below:

	    pip install opencv-python





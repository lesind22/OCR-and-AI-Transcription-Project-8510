# OCR-and-AI-Transcription-Project-8510

I am working with "The Colored American Magazine," a Black magazine publication that contributed to advocating for Black identity and representation in the early 19th century. I chose this publication because it offers a manageable starting point for experimentation. I plan to select one issue of "The Colored American Magazine," download it as a PDF, convert it to images using pdf2images, and then run it through Tesseract to perform OCR. Once I have that text, I will use OpenAI’s GPT-5-nano to process and interpret the text. I am particularly interested in observing how the model handles text with imperfect OCR, where it might help clarify content, but also where it could distort images or omit language.

To Run Scripts, these packages and dependencies must be installed via VSCode in Python:

	Tesseract
	pdf2image
	opencv-python
	OpenAI (no need to install web-based application)

_________________________________________________________________________________________________________________________________________________________________________________________

To install Tesseract on Terminal in VSCode:

  	 pip3 install pytesseract


_________________________________________________________________________________________________________________________________________________________________________________________


To install Tesseract using Homebrew in System Terminal (macOS):

  	 brew install tesseract


_________________________________________________________________________________________________________________________________________________________________________________________

Before creating your virtual environment, isolating your project's dependencies, make sure Poppler is installed via Homebrew in System Terminal (macOS):
    
     brew install poppler

_________________________________________________________________________________________________________________________________________________________________________________________
     
Before installing pdf2image, create a virtual environment in your VSCode terminal. Instructions below:
   
    python3 -m venv venv
    source .venv/bin/activate


_________________________________________________________________________________________________________________________________________________________________________________________


While installing opencv-python, make sure your virtual environment is activated. Below are the instructions to install opencv-python:
  
    source .venv/bin/activate
    pip3 install opencv-python



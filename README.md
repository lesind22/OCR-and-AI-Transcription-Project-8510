# OCR-and-AI-Transcription-Project-8510

I am working with "The Colored American Magazine," a Black magazine publication that contributed to advocating for Black identity and representation in the early 19th century. I plan to: 
        - Select one issue of "The Colored American Magazine" 
        - Download it as a PDF 
        - Convert it to images using ImageMagick
        - Run it through Tesseract to perform OCR. 
        - Once I have that text, I will use OpenAI’s GPT-5-nano to process and interpret the text 

I am particularly interested in observing how the model handles text with imperfect OCR, where it might help clarify content, but also where it could distort images or omit language.

_________________________________________________________________________________________________________________________________________________________________________________________
To Run Scripts, these packages and dependencies must be installed via VSCode in Python:

- Create a virtual environment via VSCode
- ImageMagick (Wand dependency)
- Pytesseract (Tesseract) (Pillow dependency)
- opencv-python
- OpenAI (no need to install a web-based application)

_________________________________________________________________________________________________________________________________________________________________________________________
Before installing pdf2image, create a virtual environment in your VSCode terminal. Instructions below:
   
    python3 -m venv venv
    source .venv/bin/activate

_________________________________________________________________________________________________________________________________________________________________________________________

To install Wand via Python in VSCode Terminal:

		pip install wand



To install ImageMagick via Homebrew Terminal:

		brew install imagemagick
		
_________________________________________________________________________________________________________________________________________________________________________________________

To Run Contrast and Enhancement Script "opencv-python" must be installed. Instructions below:

	pip install opencv-python





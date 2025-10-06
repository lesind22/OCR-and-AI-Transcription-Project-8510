# OCR-and-AI-Transcription-Project-8510

I will work with "The Colored American Magazine", a Black periodical published in the early twentieth century, and "Negro Digest" magazine. I chose these publications because it offers a manageable starting point for experimentation. I plan to select issuea of "The Colored American Magazine" and "Negro Digest", download them as a PDF, convert it to an image using ImageMagick, then run it through Tesseract to perform OCR. Once I have that text, I will use OpenAI’s GPT-5-nano to process and interpret the text. I am particularly interested in observing how the model handles text with imperfect OCR, where it might help clarify content, but also where it could distort images or generate harmful language.


_________________________________________________________________________________________________________________________________________________________________________________________

To install Tesseract on System:
 
  brew install Tesseract 

_________________________________________________________________________________________________________________________________________________________________________________________



Install Dependencies for ImageMagick on System:
 
  brew install wand pillow pytesseract


_________________________________________________________________________________________________________________________________________________________________________________________



To install ImageMagick on System:
 
  brew install ImageMagick ghostscript



_________________________________________________________________________________________________________________________________________________________________________________________




To Run "simple_ocr.py" Script, into Python terminal enter:

python simple_ocr.py "/Users/indiralessington/Desktop/TheColoredAmerican.pdf"

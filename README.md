# OCR-and-AI-Transcription-Project-8510

I will work with "The Colored American Magazine" and "Negro Digest", Black magazine publications advocating for the quest for Black identity and representation in the early-mid 19th century. I chose these publications because they offer a manageable starting point for experimentation. I plan to select issues of "The Colored American Magazine" and "Negro Digest", download them as a PDF, convert them to images using ImageMagick, then run them through Tesseract to perform OCR. Once I have that text, I will use OpenAI’s GPT-5-nano to process and interpret the text. I am particularly interested in observing how the model handles text with imperfect OCR, where it might help clarify content, but also where it could distort images or have offensive language.


_________________________________________________________________________________________________________________________________________________________________________________________

To install Tesseract on System (Mac OS):
 
  brew install Tesseract 

_________________________________________________________________________________________________________________________________________________________________________________________



Install Dependencies for ImageMagick on System (Mac OS):
 
  brew install wand pillow pytesseract


_________________________________________________________________________________________________________________________________________________________________________________________



To install ImageMagick on System (Mac OS):
 
  brew install ImageMagick ghostscript



_________________________________________________________________________________________________________________________________________________________________________________________




To Run "simple_ocr.py" Script, into Python terminal enter (VSCode):

python simple_ocr.py "/Users/indiralessington/Desktop/TheColoredAmerican.pdf"

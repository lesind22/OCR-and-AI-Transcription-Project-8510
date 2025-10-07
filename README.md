# OCR-and-AI-Transcription-Project-8510

I will work with "The Colored American Magazine," a Black magazine publication advocating for the quest for Black identity and representation in the early 19th century. I chose this publication because it offers a manageable starting point for experimentation. I plan to select one issue of "The Colored American Magazine," download it as a PDF, convert it to images using pdf2images, and then run it through Tesseract to perform OCR. Once I have that text, I will use OpenAI’s GPT-5-nano to process and interpret the text. I am particularly interested in observing how the model handles text with imperfect OCR, where it might help clarify content, but also where it could distort images or have offensive language.

To Run Scripts, these packages and dependencies must be installed:
_________________________________________________________________________________________________________________________________________________________________________________________

To install Tesseract on System (MacOS):
 
  brew install Tesseract 

_________________________________________________________________________________________________________________________________________________________________________________________


To install pdf2image (MacOS):
 
  python3 install pdf2image



To install dependencies for pdf2image (MacOS)

  python3 install poppler


_________________________________________________________________________________________________________________________________________________________________________________________

To install pdf2image, PIL (depndency to run pdf2image), Poppler (depndency to run pdf2image) and CV2 (MacOS):

  brew install pdf2image


  brew install PIL


  brew install poppler


  brew install cv2


_________________________________________________________________________________________________________________________________________________________________________________________




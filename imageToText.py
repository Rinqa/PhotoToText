import pytesseract as tess
#tess.pytesseract.tesseract_cmd = r'C:\Users\AllTech\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('test.jpg')
text = tess.image_to_string(img)

print(text)

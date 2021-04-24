import pytesseract
from PIL import ImageEnhance, ImageFilter
from PIL import Image as Img
im = Img.open("image.png")
im = im.filter(ImageFilter.MedianFilter())

enhancer = ImageEnhance.Contrast(im)
#aplicando filtro para mejorar la convercion de imagen->txt
im = enhancer.enhance(25)
im = im.convert('1')
im.save('sample.jpeg')

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Img.open('sample.jpeg'), lang='spa')

print(text)
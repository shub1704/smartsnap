from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def imagetotext(img):
    pic = Image.open(img)
    text = tess.image_to_string(pic)
    #print(type(text))__to check type of output
    return (text)


if __name__ == '__main__':
    text = imagetotext('snip1.png')
    print(text)
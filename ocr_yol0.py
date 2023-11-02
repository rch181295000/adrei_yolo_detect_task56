import pytesseract
import cv2
import matplotlib.pyplot as plt
import sys
from PIL import Image

# read the image using OpenCV
# from the command line first argument
image = cv2.imread('ocr_image/test.jpg')
# or you can use Pillow
# image = Image.open(sys.argv[1])
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"
# get the string
string = pytesseract.image_to_string(image)

# print it
print(string)

# get all data
data = pytesseract.image_to_data(image)

print(data)
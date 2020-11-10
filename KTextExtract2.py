from PIL import Image 
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def main():
	path = r'C:\Users\CHIJINDU\Desktop\ml learn'
	# path for the folder for getting the raw images
	# iterating the images inside the folder
	for imageName in os.listdir(path):
		inputPath= os.path.join(path, imageName)
		img_cv = cv2.imread(inputPath)
		img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)


		#img = Image.open(inputPath)
		#applying ocr using pytesseract for python
		text = pytesseract.image_to_string(img_rgb, lang='eng')
		print(text) 
        
         
main()

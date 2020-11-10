#Extract texts
import cv2
import pytesseract


def extract():
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
	img_cv = cv2.imread(r'C:\Users\CHIJINDU\Desktop\ml learn\24.jpg')

	# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
	# we need to convert from BGR to RGB format/mode:
	img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
	print(pytesseract.image_to_string(img_rgb))
# OR
#img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
#print(pytesseract.image_to_string(img_rgb))

extract()

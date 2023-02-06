import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
import cv2


image = "./pic/19.jpg"

img = Image.open(image)

# img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度

# img = ImageEnhance.Sharpness(img).enhance(20.0)#銳利化

# img = ImageEnhance.Contrast(img).enhance(4.0)#增加對比度

# img = img.convert('L')#灰度化

img.show()
# barcodes = pyzbar.decode(img)


image1 = cv2.imread('./pic/19.jpg')
img_crop = image1[540:590,716:1077]
x, y = img_crop.shape[0:2]
img_crop_test = cv2.resize(img_crop,(int(y*2),int(x*2)))
barcodes = pyzbar.decode(img_crop_test)

for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)

cv2.imshow('final',img_crop_test)
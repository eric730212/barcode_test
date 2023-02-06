import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
import cv2


image = "./pic/35.jpg"

img = Image.open(image)

img = ImageEnhance.Brightness(img).enhance(2.5)#增加亮度

# img = ImageEnhance.Sharpness(img).enhance(17.0)#銳利化

img = ImageEnhance.Contrast(img).enhance(100.0)#增加對比度

img = img.convert('L')#灰度化



img = img.crop((118,463,553,598))
img.show()
barcodes = pyzbar.decode(img)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print('ori:',barcodeData)


image1 = cv2.imread('./pic/35.jpg')
img_crop = image1[522:568,627:812]
x, y = img_crop.shape[0:2]
img_crop_test = cv2.resize(img_crop,(int(y*4),int(x*4)))
img_crop_test = cv2.cvtColor(img_crop_test, cv2.COLOR_BGR2GRAY)
barcodes = pyzbar.decode(img_crop_test)
# img_crop_test = cv2.resize(image1,(640,480) ,interpolation=cv2.INTER_AREA)
# barcodes = pyzbar.decode(img_crop_test)


for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print('corp2:',barcodeData)

# image2 = cv2.imread('./pic/23.jpg')
# img_crop = image2[225:263,314:451]
# x, y = img_crop.shape[0:2]
# img_crop_test = cv2.resize(img_crop,(int(y*2),int(x*2)))
# barcodes = pyzbar.decode(img_crop_test)
#
# for barcode in barcodes:
#     barcodeData = barcode.data.decode("utf-8")
#     print('corp2:',barcodeData)




# cv2.imshow('final',img_crop_test)
# cv2.waitKey(0)
import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np

image=cv2.imread("./pic/18.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
texts = pyzbar.decode(gray)
print(texts)
if texts==[]:
    print("未識別成功")
else:
    for text in texts:
        tt = text.data.decode("utf-8")
    print("識別成功")
    print(tt)


img = cv2.imread('./pic/18.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); # 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
output2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
output3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

texts = pyzbar.decode(output3)
print(texts)
if texts==[]:
    print("未識別成功")
else:
    for text in texts:
        tt = text.data.decode("utf-8")
    print("識別成功")
    print(tt)



cv2.imshow('oxxostudio', img)
cv2.imshow('oxxostudio1', output1)
cv2.imshow('oxxostudio2', output2)
cv2.imshow('oxxostudio3', output3)
# cv2.imshow('oxxostudio4', output4)
# cv2.imshow('oxxostudio5', output5)

cv2.waitKey(0)
cv2.destroyAllWindows()
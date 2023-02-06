import cv2
from pylibdmtx.pylibdmtx import decode

img = cv2.imread('./pic/11.jpg')
img_crop = img[478:610,782:920]
result = decode(img_crop,shrink=2,threshold=6)
print(result)
print(result[0].data.decode('utf-8'))

x=782
y=478
w=180
h=180
img2=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)

# print(decode(img_crop))


img1 = cv2.imread('./pic/1.jpg')
print(decode(img1,shrink=2,threshold=6))

cv2.destroyAllWindows()
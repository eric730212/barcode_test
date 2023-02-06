import cv2
from pylibdmtx.pylibdmtx import decode


def sharpen(img, sigma=80):
    # sigma = 5、15、25
    blur_img = cv2.GaussianBlur(img, (0, 0), sigma)
    usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)

    return usm


img = cv2.imread('./pic/1.jpg')
# img_crop = img[348:470,564:698]
img_crop = img[490:640,352:494]
print(img_crop.shape)
x, y = img_crop.shape[0:2]
img_crop_test = cv2.resize(img_crop,(int(y*2),int(x*2)))
# result = decode(img_crop,shrink=2,threshold=6)
result = decode(img_crop_test)

print(result)
print(len(result))
result_text = str(result[0].data,"utf-8")
print(result_text)


# for i in range(len(result)):
#     print(result[i].data)
#     print(str(result[i].data, "utf-8")) #removes the b'... formatting
#     print(result[i].rect.left)
#     print(result[i].rect.top)
#     print(result[i].rect.width)
#     print(result[i].rect.height)



#
cv2.imshow('crop',img_crop_test)
cv2.imshow('crop_sharpen',sharpen(img_crop_test))
# print(result[0].data.decode('utf-8'))
#
#
img2=cv2.rectangle(img, (1202,589), (1285,660), (0, 255, 0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)
#
# print(decode(img_crop))



cv2.destroyAllWindows()


import cv2



im = cv2.imread('./pic/16.jpg')
# im_crop = im[478:130,782:138]
im_crop = im[478:610,782:920]
# red_color = (0,0,255)
# cv2.rectangle(im,(782,478),(920,610),red_color,3,cv2.LINE_AA)

cv2.imshow('im',im_crop)
cv2.waitKey(0)
import cv2

img = './pic/13.jpg'
img = cv2.imread(img)
cv2.imshow('original', img)

# 選擇ROI
roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
print(roi)

# 顯示ROI並儲存圖片
if roi != (0, 0, 0, 0):
    crop = img[y:y+h, x:x+w]
    cv2.imshow('crop', crop)
    cv2.imwrite('./pic/12.jpg', crop)
    print('Saved!')

# 退出
cv2.waitKey(0)
cv2.destroyAllWindows()
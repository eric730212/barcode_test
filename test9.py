# 儲存縮圖

from PIL import Image
bg = Image.new('RGB',(2400, 1600), '#000000') # 產生一張 1200x800 的全黑圖片
for i in range(1,9):
    img = Image.open(f'./pic/{i}.jpg')  # 開啟圖片
    img = img.resize((600, 800))   # 縮小尺寸為 300x400
    x = (i-1)%4                    # 根據開啟的順序，決定 x 座標
    y = (i-1)//4                   # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(img,(x*600, y*800))   # 貼上圖片

# cv2.imshow('bg',bg)
# cv2.waitKey(0)
bg.save('C:\\Users\\Server\\PycharmProjects\\barcode_test\\pic\\combine.jpg')
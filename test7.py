import cv2
from pylibdmtx.pylibdmtx import decode

camera = cv2.VideoCapture(1)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
camera.set(cv2.CAP_PROP_FPS, 10)
# ret, frame = camera.read()

# while True:
#     ret, frame = camera.read()
#     try:
#         x = 864
#         y = 248
#         w = 1100 - 864
#         h = 470 - 248
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         dmtx = decode(frame[248:470, 864:1100], shrink=1, threshold=100)
#         print(dmtx)
#         print(dmtx[0].data.decode('utf-8'))
#     except:
#         print('X')
#
#     # print(decode(frame,shrink=2,threshold=6))
#     if (cv2.waitKey(5) == 27):
#         break
#     cv2.imshow('frame', frame)

ret, frame = camera.read()
try:
    x = 864
    y = 640
    w = 1100 - 864
    h = 840 - 640
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    dmtx = decode(frame[640:840, 864:1100], shrink=1, threshold=100)
    print(dmtx)
    print(dmtx[0].data.decode('utf-8'))
except:
    print('X')

# print(decode(frame,shrink=2,threshold=6))

cv2.imshow('frame', frame)
cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2
import time

try:
    cap1 = cv2.VideoCapture(0)
except:
    print('cam1 error')
try:
    cap2 = cv2.VideoCapture(1)
except:
    print('cam2 error')
try:
    cap3 = cv2.VideoCapture(2)
except:
    print('cam3 error')
try:
    cap4 = cv2.VideoCapture(3)
except:
    print('cam4 error')
try:
    cap5 = cv2.VideoCapture(4)
except:
    print('cam5 error')
try:
    cap6 = cv2.VideoCapture(5)
except:
    print('cam6 error')
try:
    cap7 = cv2.VideoCapture(6)
except:
    print('cam7 error')
try:
    cap8 = cv2.VideoCapture(7)
except:
    print('cam7 error')


while True:
    # cap1 = cv2.VideoCapture(0)
    # cap2 = cv2.VideoCapture(1)
    # cap3 = cv2.VideoCapture(2)
    # cap4 = cv2.VideoCapture(3)
    # cap5 = cv2.VideoCapture(4)
    # cap6 = cv2.VideoCapture(5)

    ret, frame1 = cap1.read()
    print('ret1:',ret)
    # cap1.release()
    ret2, frame2 = cap2.read()
    print('ret2:',ret2)
    # # cap2.release()
    ret3, frame3 = cap3.read()
    print('ret3:', ret3)
    # # cap3.release()
    ret4, frame4 = cap4.read()
    print('ret4:', ret4)
    # # cap4.release()
    ret5, frame5 = cap5.read()
    print('ret5:', ret5)
    # # cap5.release()
    ret6, frame6 = cap6.read()
    print('ret6:', ret6)
    # # cap6.release()
    ret7, frame7 = cap7.read()
    print('ret7:', ret7)
    ret8, frame8 = cap8.read()
    print('ret8:', ret8)


    cv2.imshow('cam1', frame1)
    cv2.imshow('cam2', frame2)
    cv2.imshow('cam3', frame3)
    cv2.imshow('cam4', frame4)
    cv2.imshow('cam5', frame5)
    cv2.imshow('cam6', frame6)
    cv2.imshow('cam7', frame7)
    cv2.imshow('cam8', frame8)



    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()


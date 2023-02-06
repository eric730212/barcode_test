import cv2

camera = cv2.VideoCapture(1,cv2.CAP_DSHOW)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while(True):
    retval, im = camera.read()
    if im.any(): # errors out when image is none
        cv2.imshow("image", im)

    k = cv2.waitKey(33)
    if k==27: # Esc key press
        print('Resolution: {0}x and {1}y'.format(im.shape[1],im.shape[0]))
        print('FPS: {0}'.format(camera.get(cv2.CAP_PROP_FPS)))
        break

camera.release()
cv2.destroyAllWindows()
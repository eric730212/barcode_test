import cv2

camera=0
cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1050)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    cv2.imshow('Image', image)
    if cv2.waitKey(5) & 0xFF == ord("q"):
      break
cap.release()
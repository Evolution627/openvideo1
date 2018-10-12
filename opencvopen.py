import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MYwindow')
cv2.setMouseCallback('MYwindow',onMouse)

print("Showing camera feed. CLick widnow or press any key to stop.")

success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('MYwindow',frame)
    success, frame = cameraCapture.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # eyes = eye_cascade.detectMultiScale(gray,1.1,5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) # blue,green,red

cv2.destroyWindow('MYwindow')
cameraCapture.release()

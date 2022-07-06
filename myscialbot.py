import cv2


cap = cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
key = -1

while key == -1:
    isRead, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    print(faces)

    key = cv2.waitkey(20)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiscale(image_gray)
    print(faces)
    cv2.imshow('window', image)
    key .cv2.waitkey (20)
    cap.release()
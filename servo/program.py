import cv2
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
tilt = 18
GPIO.setup(tilt, GPIO.OUT)
angle=90

def setServoAngle(servo, angle):
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()



setServoAngle(tilt, 90)


X_center = 90
X_left = 70
X_right = 110
pos = 0
old_pos = 0

# Большой серво 3 - 10
# Малый серво   6 - 4
# OpenCV
cap = cv2.VideoCapture(2)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    setServoAngle(tilt, angle)
    isRead, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, minNeighbors=15)
    for face in faces:
        x, y, w, h = face
        c_x = x + (w / 2)
        c_y = y + (h / 2)
        cv2.circle(image, (int(c_x), int(c_y)), 3, (0, 200, 0), 2)

        if c_x > 420:
            pos = 'left'
        elif c_x < 220:
            pos = 'right'
        elif c_x < 420 and c_x > 220:
            pos = 'center'

        if old_pos != pos:
            if pos == 'center':
                print("X_center", X_center)
                # setServoAngle(tilt, X_center)
            if pos == 'right':
                print("X_center", X_right)
                if angle >70:
                    angle = angle - 20
                # setServoAngle(tilt, X_right)
            if pos == 'left':
                print("X_center", X_left)
                angle=angle+20
                # setServoAngle(tilt, X_left)
            old_pos = pos
        # print(X_turn)
    cv2.imshow("image", image)
    if cv2.waitKey(20) & 0xFF == ord(' '):
        break

GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()

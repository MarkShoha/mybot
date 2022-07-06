import cv2
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
tilt = 18
GPIO.setup(tilt, GPIO.OUT)

def setServoAngle(servo, angle):
	assert angle >=30 and angle <= 150
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()

if __name__ == '__main__':
	i = int(input("ввод: "))
	setServoAngle(tilt, i)
	GPIO.cleanup()
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
BigServo_Pin = 17
GPIO.setup(BigServo_Pin, GPIO.OUT)
BigServo = GPIO.PWM(BigServo_Pin, 50)
BigServo.ChangeDutyCycle(6)
time.sleep(2)
BigServo.stop()
GPIO.cleanup()

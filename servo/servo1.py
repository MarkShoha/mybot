from rpi_hardware_pwm import HardwarePWM
import time
pwm = HardwarePWM(pwm_channel=0, hz=60)
pwm.start(5.5)
while True:
    i = float(input("введите число: "))
    pwm.change_duty_cycle(i)
    time.sleep(2)
    pwm.stop()


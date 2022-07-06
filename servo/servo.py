from rpi_hardware_pwm import HardwarePWM
import time
pwm = HardwarePWM(pwm_channel=0, hz=50)
pwm.start(100)
for i in range(3):
    pwm.change_duty_cycle(3)
    time.sleep(1)
    pwm.change_duty_cycle(6)
    time.sleep(1)
    pwm.change_duty_cycle(12)
    time.sleep(1)
pwm.stop()

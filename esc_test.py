# esc test code(esc_test.py)
# result : worked well at motor, but stop the code it worked slowly

import pigpio
import time

ESC_PIN = 13
pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC_PIN, 0)
time.sleep(1)

print("Sending min throttle (1000)")
pi.set_servo_pulsewidth(ESC_PIN, 1000)
time.sleep(0.5) # it was 2 sec 

print("Sending mid throttle (1500)")
pi.set_servo_pulsewidth(ESC_PIN, 1500)
time.sleep(0.5) # it was 3 sec

print("Stopping")
pi.set_servo_pulsewidth(ESC_PIN, 0)
pi.stop()

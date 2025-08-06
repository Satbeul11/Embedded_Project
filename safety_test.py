import pigpio
import time

pi = pigpio.pi()
ESC_PIN = 13
pi.set_servo_pulsewidth(ESC_PIN, 0)

try:
    pi.set_servo_pulsewidth(ESC_PIN, 1100)
    time.sleep(2)
    pi.set_servo_pulsewidth(ESC_PIN, 1200)
    time.sleep(2)
    pi.set_servo_pulsewidth(ESC_PIN, 1300)
    time.sleep(2)
except KeyboardInterrupt:
    print("Emergency stop!")
finally:
    pi.set_servo_pulsewidth(ESC_PIN, 0)
    pi.stop()
    print("PWM signal stopped.")  

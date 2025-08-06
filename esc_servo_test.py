# test code(esc_servo_test.py)
# result : servo working, motor not working

import pigpio
import time

pi = pigpio.pi()

ESC_PIN = 13     # GPIO13 (ESC)
SERVO_PIN = 12   # GPIO12 (Servo)

# 초기화
pi.set_servo_pulsewidth(ESC_PIN, 0)
pi.set_servo_pulsewidth(SERVO_PIN, 0)

# ESC 암 (arming)
pi.set_servo_pulsewidth(ESC_PIN, 1000)  # 최소 스로틀
time.sleep(2)
pi.set_servo_pulsewidth(ESC_PIN, 1500)  # 중간
time.sleep(2)

# Servo 테스트
print("Moving servo...")
pi.set_servo_pulsewidth(SERVO_PIN, 1000)  # 왼쪽
time.sleep(1)
pi.set_servo_pulsewidth(SERVO_PIN, 2000)  # 오른쪽
time.sleep(1)
pi.set_servo_pulsewidth(SERVO_PIN, 1500)  # 중간
time.sleep(1)

# 정지
pi.set_servo_pulsewidth(ESC_PIN, 0)
pi.set_servo_pulsewidth(SERVO_PIN, 0)
pi.stop()

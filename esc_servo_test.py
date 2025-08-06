# esc_servo_test.py
# Result: servo + ESC test with safe shutdown on Ctrl+C

import pigpio
import time

ESC_PIN = 13     # GPIO13 for ESC
SERVO_PIN = 12   # GPIO12 for Servo

pi = pigpio.pi()

try:
    # Initialize
    pi.set_servo_pulsewidth(ESC_PIN, 0)
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    time.sleep(0.5)

    # Arm ESC
    print("Arming ESC...")
    pi.set_servo_pulsewidth(ESC_PIN, 1000)
    time.sleep(1)
    pi.set_servo_pulsewidth(ESC_PIN, 1500)
    time.sleep(1)

    # Servo test
    print("Moving servo...")
    pi.set_servo_pulsewidth(SERVO_PIN, 1000)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(SERVO_PIN, 2000)
    time.sleep(0.5)
    pi.set_servo_pulsewidth(SERVO_PIN, 1500)
    time.sleep(0.5)

    # Hold state until user ends
    input("Press Enter or Ctrl+C to stop...")

except KeyboardInterrupt:
    print("\n[!] Ctrl+C received — stopping motors.")

finally:
    # Always stop on exit
    pi.set_servo_pulsewidth(ESC_PIN, 0)
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()
    print("✅ ESC and Servo stopped safely.")

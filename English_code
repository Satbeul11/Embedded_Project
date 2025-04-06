import RPi.GPIO as GPIO
import time

# Pin configuration
LIGHT_SENSOR_PIN = 18  # Light sensor (digital)
SERVO_PIN = 17         # Servo motor

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

# Servo motor setup
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz
servo.start(0)

# Function to set servo angle
def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(SERVO_PIN, False)
    servo.ChangeDutyCycle(0)

try:
    while True:
        light_detected = GPIO.input(LIGHT_SENSOR_PIN)
        if light_detected == GPIO.HIGH:
            print("Bright - Lowering blinds")
            set_servo_angle(90)  # Lower the blinds
        else:
            print("Dark - Raising blinds")
            set_servo_angle(0)   # Raise the blinds
        time.sleep(2)

except KeyboardInterrupt:
    print("Program terminated")
    GPIO.cleanup()

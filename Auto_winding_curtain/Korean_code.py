import RPi.GPIO as GPIO
import time

# 핀 번호 설정
LIGHT_SENSOR_PIN = 18  # 조도센서
SERVO_PIN = 17         # 서보모터

# 서보모터 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz

# 조도센서 설정
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

servo.start(0)

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
            print("밝음 - 블라인드 내림")
            set_servo_angle(90)  # 블라인드 내리기
        else:
            print("어두움 - 블라인드 올림")
            set_servo_angle(0)   # 블라인드 올리기
        time.sleep(2)

except KeyboardInterrupt:
    print("종료합니다")
    GPIO.cleanup()

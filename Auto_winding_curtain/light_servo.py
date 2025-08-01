import smbus
import time
import RPi.GPIO as GPIO

# I2C 설정
bus = smbus.SMBus(1)
address = 0x48

# 서보 핀 설정
SERVO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.3)
    pwm.ChangeDutyCycle(0)  # 서보 떨림 방지용

try:
    while True:
        bus.write_byte(address, 0x40)   # AIN0 = 조도센서
        bus.read_byte(address)
        value = bus.read_byte(address)
        print("조도 값:", value)

        if value < 100:
            set_angle(90)  # 서보를 90도로 이동
        else:
            set_angle(0)   # 서보를 0도로 복귀

        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

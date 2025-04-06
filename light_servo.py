import smbus
import time

bus = smbus.SMBus(1)
address = 0x48

while True:
    bus.write_byte(address, 0x40)       # AIN0 = 조도센서
    bus.read_byte(address)              # 더미 읽기
    value = bus.read_byte(address)      # 실제 조도값
    print("조도 값:", value)
    time.sleep(0.5)

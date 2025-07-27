from machine import Pin, PWM
import time

# 모터 핀 설정
M1 = PWM(Pin(4), freq=10000, duty=0)
M2 = PWM(Pin(5), freq=10000, duty=0)
M3 = PWM(Pin(40), freq=10000, duty=0)
M4 = PWM(Pin(41), freq=10000, duty=0)

M1.duty(800)
M3.duty(800)
time.sleep(1)
M1.duty(0)
M3.duty(0)

for m in [M1, M2, M3, M4]:
    m.deinit()
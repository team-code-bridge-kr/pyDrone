from machine import Pin, PWM
import time

M1 = PWM(Pin(4), freq=10000, duty=0)1

M1.duty(200)
time.sleep(1)

M1.duty(500)
time.sleep(1)

M1.duty(1000)
time.sleep(1)

M1.deinit()
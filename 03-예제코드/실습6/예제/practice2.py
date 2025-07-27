import network
import socket
import time
from machine import Pin, PWM

# AP 모드 설정
wlan_ap = network.WLAN(network.AP_IF)
wlan_ap.active(True)
wlan_ap.config(essid="pyDrone-Joystick", authmode=0)
while not wlan_ap.active():
    time.sleep(1)
print("AP 모드 실행 중:", wlan_ap.ifconfig())

# 모터 세팅
M1 = PWM(Pin(4), freq=10000, duty=0)
M2 = PWM(Pin(5), freq=10000, duty=0)
M3 = PWM(Pin(40), freq=10000, duty=0)
M4 = PWM(Pin(41), freq=10000, duty=0)

base_speed = 600

def stop_all():
    M1.duty(0)
    M2.duty(0)
    M3.duty(0)
    M4.duty(0)

def set_motors(m1, m2, m3, m4):
    M1.duty(max(0, min(1023, m1)))
    M2.duty(max(0, min(1023, m2)))
    M3.duty(max(0, min(1023, m3)))
    M4.duty(max(0, min(1023, m4)))

def handle_command(cmd):
    cmd = cmd.strip().upper()
    print("명령 수신:", cmd)
    if cmd == "TAKEOFF":
        set_motors(base_speed+200, base_speed+200, base_speed+200, base_speed+200)
    elif cmd == "W":
        set_motors(base_speed+100, base_speed+100, base_speed, base_speed)
    elif cmd == "S":
        set_motors(base_speed, base_speed, base_speed+100, base_speed+100)
    elif cmd == "A":
        set_motors(base_speed, base_speed+100, base_speed, base_speed+100)
    elif cmd == "D":
        set_motors(base_speed+100, base_speed, base_speed+100, base_speed)
    elif cmd == "H":
        set_motors(base_speed, base_speed, base_speed, base_speed)
    elif cmd == "LAND":
        for speed in range(base_speed+200, -1, -100):
            set_motors(speed, speed, speed, speed)
            time.sleep(0.3)
        stop_all()
    elif cmd == "HOVER":
        m1.duty_u16(30000)
        m2.duty_u16(30000)
        m3.duty_u16(30000)
        m4.duty_u16(30000)

    elif cmd == "STOP":
        stop_all()

# UDP 소켓 생성
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("0.0.0.0", 10000))
print("UDP 서버 대기 중...")

while True:
    data, addr = udp.recvfrom(1024)
    handle_command(data.decode('utf-8'))

import network
import socket
import time

wlan_ap = network.WLAN(network.AP_IF)
wlan_ap.active(True)
Wlan_ap.config(essid='네트워크명입력', automode=0)
print("AP 모드 시작: ", wlan_ap.ifconfig())

udp소켓 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp소켓.bind(('0.0.0.0', 2390))
print("UDP 서버 대기중 (포트 2390)")


while True:
    data, addr = udp소켓.recvfrom(128)
    print("수신:", data)
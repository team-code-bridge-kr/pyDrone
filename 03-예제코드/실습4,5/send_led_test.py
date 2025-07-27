import socket
import time

HOST = "192.168.4.1"
PORT = 2390

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:
    sock.sendto(b'on', (drone_ip, drone_port))
    print("LED ON 명령 전송 완료")

    data, addr = sock.recvfrom(128)
    print("드론 응답 : ", data.decode())

    sock.sendto(b'off', (drone_ip, drone_port))
    print("LED OFF 명령 전송 완료")

    data, addr = sock.recvfrom(128)
    print("드론 응답 : ", data.decode())

finally:
    sock.close()
import socket

# ESP32의 AP 모드 IP 주소
HOST = "192.168.4.1"  # ESP32 기본 AP 모드 IP
PORT = 2390          # ESP32 UDP 포트

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_udp_command(cmd):
    sock.sendto(cmd.encode('utf-8'), (HOST, PORT))

if __name__ == "__main__":
    print("PyDrone 조이스틱 클라이언트 (Q 입력 시 종료)")
    while True:
        cmd = input("명령 입력 (TAKEOFF / W / A / S / D / HOVER / H / LAND / STOP): ").strip().upper()
        if cmd == "Q":
            print("종료합니다.")
            break
        send_udp_command(cmd)

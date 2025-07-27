# === main.py Autonomous A-B 왕복 ===

import network
import time
from machine import Timer
import drone

# === 드론 객체 생성 ===
드론 = drone.DRONE(flightmode=0)

# ========================================================
# 1) IMU 칼리브레이션(수평 교정) 대기 함수
# ========================================================
def 교정_대기():
    while True:
        데이터 = 드론.read_cal_data()
        print("칼리브레이션 데이터:", 데이터)
        if 드론.read_calibrated():
            완료데이터 = 드론.read_cal_data()
            print("교정 완료:", 완료데이터)
            break
        time.sleep_ms(100)

# ========================================================
# 2) WiFi AP 모드 설정 (선택사항)
# ========================================================
def AP_시작():
    wlan_ap = network.WLAN(network.AP_IF)
    print('"pyDrone" AP 모드로 전환 중...')
    wlan_ap.active(True)
    wlan_ap.config(essid='pyDrone', authmode=0)
    while not wlan_ap.active():
        pass
    print("AP 모드 시작 완료, IP 정보:", wlan_ap.ifconfig())

# ========================================================
# 3) A-B 왕복 이동 함수
# ========================================================
def 왕복_비행():
    print("=== 드론 왕복 비행 시작 ===")

    # === 1. 이륙
    print("이륙 중...")
    드론.take_off(distance=120)
    time.sleep(2)

    # === 2. A -> B (전진)
    print("B 지점으로 이동...")
    for i in range(30):  # 이동시간 조절
        드론.control(rol=0, pit=+30, yaw=0, thr=0)
        time.sleep(0.1)

    # === 3. B -> A (후진)
    print("A 지점으로 복귀...")
    for i in range(30):  # 이동시간 조절
        드론.control(rol=0, pit=-30, yaw=0, thr=0)
        time.sleep(0.1)

    # === 4. 호버링 후 착륙
    print("호버링...")
    드론.control(rol=0, pit=0, yaw=0, thr=0)
    time.sleep(2)

    print("착륙 중...")
    드론.landing()

    print("=== 왕복 비행 완료 ===")

# ========================================================
# 4) 실행 순서
# ========================================================
교정_대기()
AP_시작()  # Wi-Fi 필요시만 호출

왕복_비행()

print("프로그램 종료 (USB 제거 후에도 실행되도록 main.py에 저장 필요)")


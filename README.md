# pyDrone

> 본 프로젝트는 TeamCodeBridge가 01Studio의 PyDrone 공식 위키 예제를 참고하여, 한국어 번역 및 주석 처리로 재구성한 교육용 자료입니다.


## 1. Thonny IDE 설치

개발 소프트웨어는 코드를 작성하기 위한 도구입니다. pyDrone 개발에는 공식 추천 **Thonny Python IDE**를 사용합니다.

* **특징**

  * 오픈 소스, 미니멀 설계
  * MicroPython 호환
  * Windows, Mac OS, Linux, Raspberry Pi 지원
* **설치 경로**

  * 01-개발도구 > 01-Windows > MicroPython IDE > Thonny
  * 또는 [https://thonny.org/](https://thonny.org/) 에서 최신 버전 다운로드
  
* **설치 방법**

  1. 설치 파일 다운로드 후 더블클릭
  2. 설치 완료 후 바탕화면 아이콘 확인
  3. Thonny 실행
> **설치 완료 메시지**: "여기까지, Thonny 설치가 완료되었습니다."
<img width="1562" height="1008" alt="image" src="https://github.com/user-attachments/assets/62bb4103-0be6-4b91-ac2c-e567e47658ee" />


## 2. 드라이버 설치

pyDrone은 ESP32-S3의 USB 가상 직렬 포트로 개발 보드와 연결됩니다.
<img width="1300" height="901" alt="image" src="https://github.com/user-attachments/assets/a6ef7d65-e7d9-4349-8e0e-a11ecf46b643" />

1. MicroUSB 케이블로 PC 연결 및 전원 공급
2. PC에서 자동 드라이버 설치
3. 내 컴퓨터 우클릭 → **속성** → **장치 관리자** 확인

   * 직렬 COM 포트가 나타나면 설치 성공
  

<img width="1300" height="901" alt="image" src="https://github.com/user-attachments/assets/74515888-4160-49b2-9697-0357d6d2dede" />


## 3. REPL 직렬 포트 상호 디버깅

Thonny의 REPL(Read-Eval-Print Loop)을 통해 보드를 직접 디버깅합니다.

1. Thonny 실행 후 보드 연결
<img width="1562" height="1008" alt="image" src="https://github.com/user-attachments/assets/cf05f2c0-fa66-4ad9-b24d-ec4a8b209f96" />

2. 우측 하단 클릭 → **Configure interpreter**
3. **MicroPython (ESP32)** 및 해당 보드 선택 → 확인
<img width="776" height="336" alt="image" src="https://github.com/user-attachments/assets/320c00ae-db6a-472b-a1dc-0cf3a15a65c0" />

4. 연결 성공 시 쉘에서 펌웨어 정보 출력
<img width="1164" height="956" alt="image" src="https://github.com/user-attachments/assets/441d69cc-5a2d-4041-837a-5e809fdc294d" />


5. 아래와 같은 오류 발생 시 드라이버 및 인터프리터 설정 확인
<img width="1235" height="1083" alt="image" src="https://github.com/user-attachments/assets/81c7df37-4327-47b3-b85d-bb13b78cbf68" />


6. 필요 시 ‘실행 중단’ 혹은 리셋 키로 REPL 재시작
<img width="1230" height="517" alt="image" src="https://github.com/user-attachments/assets/bb665711-6f11-4751-8e9b-a8c5d3b7e9a2" />

!! 만약에 이렇게 했음에도 오류가 지속된다면, 펌웨어 업데이트 도구를 사용하여 펌웨어를 다시 설치해야합니다 !!
>  펌웨어 업데이트 도구 경로: 01-개발도구 > 01-Windows > Firmware update tool




### 터미널 테스트

```python
from machine import Pin
LED = Pin(46, Pin.OUT) 
LED.value(1) 
```
<img width="1226" height="373" alt="image" src="https://github.com/user-attachments/assets/19ba21d1-699a-4ccd-afb7-21ff03cee7f5" />

위 코드를 입력하고 디버깅을 하면 드론에 있는 LED가 켜지는 것을 확인할 수 있습니다.
<img width="1319" height="994" alt="image" src="https://github.com/user-attachments/assets/ce87c07a-8154-4e7a-9ac0-7b69c7d06dd4" />

## 4. 파일 시스템 관리

Thonny에서 보드의 파일 시스템을 읽고 쓸 수 있습니다.

1. 상단 메뉴 → **Files** 클릭
<img width="1644" height="1175" alt="image" src="https://github.com/user-attachments/assets/e3ecd46d-c926-44b9-a98f-544004d48878" />


2. 로컬/보드 파일 창 표시

<img width="1892" height="1330" alt="image" src="https://github.com/user-attachments/assets/817f5615-25d7-41ca-8ab3-9e9cc541253b" />

3. 드롭다운 → Flash 저장 공간 확인
 <img width="1031" height="657" alt="image" src="https://github.com/user-attachments/assets/5f809c40-831e-4ac2-a74e-50d73f5a76f3" />

<img width="688" height="424" alt="image" src="https://github.com/user-attachments/assets/127a0bc3-ba7e-428e-ac04-de3dd8293a95" />

   * 총 6M 중 펌웨어 2M 사용
4. 파일 업로드 및 삭제, 다운로드 가능


## 5. 와이파이를 이용한 드론 제어

WiFi 방식을 이용해 pyDrone을 원격 제어합니다.
>  와이파이 조종 파일 경로: 02-코드 > WiFi_Control > pyDrone > main.py


## 주요 기능
- **UDP 소켓 통신**: 컨트롤러로부터 제어 명령(롤, 피치, 요, 쓰로틀) 수신  
- **칼리브레이션 확인**: IMU 센서 자동 교정 후 비행 준비  
- **이륙/착륙/긴급정지**: 버튼 입력 처리  
- **상태 피드백**: 드론 자세(9개 상태) 데이터를 컨트롤러로 전송  
- **50ms 주기 실행**: 기체 안정적인 제어 주기 유지  

## 설치 및 실행
1. **보드 연결**  
   - Thonny IDE에서 PyDrone 보드를 USB로 연결하거나,  
     WiFi AP 모드(`pyDrone`)로 무선 연결합니다.

2. **코드 업로드**  
   - Thonny 에디터에서 `main.py`를 열고,  
     PyDrone 보드로 저장합니다.

3. **드론 AP 연결**  
   - PC 또는 모바일 기기에서 WiFi 네트워크 `pyDrone`에 연결합니다.

4. **제어 시작**  
   - 보드가 AP 모드 전환 후, 첫 UDP 패킷을 보내면  
     드론이 자동으로 컨트롤러 주소를 인지합니다.  
   - 이후 키보드(또는 사용자 정의 스크립트)를 통해  
     2390 포트로 `throttle,roll,pitch,yaw` 형식의 CSV 명령을 전송합니다.

5. **버튼 명령**  
   - `Y` 버튼 (`데이터[5] == 24`): 이륙 (120cm 고도)  
   - `A` 버튼 (`데이터[5] == 72`): 착륙  
   - `X` 버튼 (`데이터[5] == 136`): 긴급 정지  
   - `B` 버튼 (`데이터[5] == 40`): 사용자 정의 기능 (확장 가능)  

## 주의 사항
- 실제 비행 전 충분한 공간과 안전 상황을 확보하세요.  
- `main.py` 내부의 포트 번호(2390) 및 기타 설정은  
  환경에 맞게 조정 가능합니다.

import RPi.GPIO as GPIO # 필요한 라이브러리를 불러옵니다.
import time

SERVO_PIN = 13 # 서보모터를 PWM으로 제어할 핀 번호 설정
GPIO.setwarnings(False) # 불필요한 warning 제거
GPIO.setmode(GPIO.BCM) # GPIO핀의 번호 모드 설정
GPIO.setup(SERVO_PIN, GPIO.OUT) # 서보핀의 출력 설정
servo = GPIO.PWM(SERVO_PIN,50) # PWM 인스턴스 servo 생성, 주파수 50으로 설정
servo.start(0) # PWM 듀티비 0 으로 시작


def water():
    # 듀티비를 변경하여 서보모터를 원하는 만큼 움직임
    servo.ChangeDutyCycle(7.5) # 90도
    time.sleep(10)
    servo.ChangeDutyCycle(12.5) # 180도
    time.sleep(5)

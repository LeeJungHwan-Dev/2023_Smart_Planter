import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) # PWM 18번 GPIO 포트

Led = GPIO.PWM(18,60) # 60헤르츠 LED 스타트
Led.start(0)

def changeLed(pow):
    Led.ChangeDutyCycle(int(pow))



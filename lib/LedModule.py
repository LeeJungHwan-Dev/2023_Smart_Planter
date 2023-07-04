import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) # PWM 18번 GPIO 포트
GPIO.setup(12, GPIO.OUT) # PWM 12번 GPIO 포트
GPIO.setup(13, GPIO.OUT) # PWM 13번 GPIO 포트

Led_R = GPIO.PWM(18,120) # 120헤르츠 LED 스타트 12 13
Led_G = GPIO.PWM(12,120)
Led_B = GPIO.PWM(13,120)

Led_R.start(0)
Led_G.start(0)
Led_B.start(0)

def changeLed_R(pow):
    Led_R.ChangeDutyCycle(int(pow))

def changeLed_G(pow):
    Led_G.ChangeDutyCycle(int(pow))

def changeLed_B(pow):
    Led_B.ChangeDutyCycle(int(pow))

def changeLed_L(state,r,g,b):
    global Led_R, Led_G, Led_B
    if state == "ON":
        Led_R.ChangeDutyCycle(r)
        Led_G.ChangeDutyCycle(g)
        Led_B.ChangeDutyCycle(b)
    else:
        Led_R.ChangeDutyCycle(0)
        Led_G.ChangeDutyCycle(0)
        Led_B.ChangeDutyCycle(0)
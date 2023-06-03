from time import sleep
from picamera import PiCamera
from datetime import datetime

def takePic():
    # 현재 날짜와 시간 가져오기
    now = datetime.now()

    # PiCamera 객체 생성
    camera = PiCamera()

    # 사진 촬영 및 저장
    camera.capture(now+'photo.jpg')

    # 카메라 종료
    camera.stop_preview()
    camera.close()

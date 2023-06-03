from time import sleep
from picamera import PiCamera

def takePic():

    # PiCamera 객체 생성
    camera = PiCamera()

    # 사진 촬영 및 저장
    camera.capture('photo.jpg')

    # 카메라 종료
    camera.close()

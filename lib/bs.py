import Adafruit_BMP.BMP085 as BMP085
import datetime
import lib.UploadModule as upload
import lib.CameraModule as camera
import lib.ServerModule as server
import lib.LedModule as led
import spidev
import time
import threading
from firebase_admin import credentials
from firebase_admin import firestore, storage
import firebase_admin
import uuid

delay = 0.5
ldr_channel = 0
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

db = None

# Firebase 앱 초기화 함수
def initialize_firebase_app():
    global db
    if not firebase_admin._apps:
        # Firebase 서비스 계정 키 파일의 경로
        cred = credentials.Certificate("smart-planter-cde3d-firebase-adminsdk-4p05t-46a217b1d6.json")

        # Firebase 앱 초기화
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'smart-planter-cde3d.appspot.com'
        })

    # Firebase 앱 가져오기
    db = firestore.client()

# 데이터 업로드 함수
def upload_data_to_firestore(temp, pressure):
    now = datetime.datetime.now()
    today = now.strftime("%Y년 %m월 %d일")  # 현재 날짜를 "YYYY년 MM월 DD일" 형식으로 포맷팅

    doc_ref = db.collection(u"atx_t").document(today)
    doc_ref.set({
        "state": str(temp) + str(pressure)
    })

# BMP 센서 데이터 업데이트 함수
def updateBMP():
    sensor = BMP085.BMP085(busnum=1)

    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()

    temp_str = '온도: {:.2f} *C '.format(temp)
    pressure_str = '기압: {:.2f} Pa'.format(pressure)

    upload_data_to_firestore(temp_str, pressure_str)

# Firebase Storage의 bucket 객체 초기화
bucket = storage.bucket()

def get_time():
    doc_ref = db.collection(u"atx").document(u'Time')
    doc = doc_ref.get()

    if doc.exists:
        doc_dict = doc.to_dict()
        if "time" in doc_dict:
            return doc_dict["time"]

    return None

def get_R_value():
    doc_ref = db.collection(u"atx").document(u'LED_R')
    doc = doc_ref.get()

    if doc.exists:
        doc_dict = doc.to_dict()
        if "R" in doc_dict:
            return int(doc_dict["R"])

    return None

def get_G_value():
    doc_ref = db.collection(u"atx").document(u'LED_G')
    doc = doc_ref.get()

    if doc.exists:
        doc_dict = doc.to_dict()
        if "G" in doc_dict:
            return int(doc_dict["G"])

    return None

def get_B_value():
    doc_ref = db.collection(u"atx").document(u'LED_B')
    doc = doc_ref.get()

    if doc.exists:
        doc_dict = doc.to_dict()
        if "B" in doc_dict:
            return int(doc_dict["B"])

    return None

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1

    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def get_LED_value():
    doc_ref = db.collection(u"atx").document(u'LED')
    doc = doc_ref.get()

    if doc.exists:
        doc_dict = doc.to_dict()
        if "LED" in doc_dict:
            return doc_dict["LED"]

    return None

def checkLight():
    while True:
        ldr_value = readadc(ldr_channel)
        if ldr_value < 370 and get_LED_value() == "ON":
            R = get_R_value()
            G = get_G_value()
            B = get_B_value()
            led.changeLed_L("ON", R, G, B)
        else:
            led.changeLed_L("OFF", 0, 0, 0)
        time.sleep(delay)

# Firebase 앱 초기화
initialize_firebase_app()

# BMP 데이터 업데이트를 실행하는 쓰레드 생성
def run_update_bmp():
    while True:
        try:
            camera.takePic()
            upload.upload_file("photo.jpg", str(uuid.uuid4()) + ".png")
            updateBMP()
            time.sleep(get_time())
        except Exception as e:
            print("Error occurred:", str(e))

bmp_thread = threading.Thread(target=run_update_bmp)

# LED 상태 체크를 실행하는 쓰레드 생성
light_thread = threading.Thread(target=checkLight)

# 쓰레드 시작
bmp_thread.start()
light_thread.start()

# 메인 스레드 유지
while True:
    pass
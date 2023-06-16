import firebase_admin
import threading
import lib.LedModule as led
from firebase_admin import credentials
from firebase_admin import firestore

db = None
callback_done = threading.Event()

def update():
    doc_ref = db.collection(u'atx').document(u'LED_d')
    doc_ref.update({u'init_pow': u'50'})

def getPow_R():
    docs = db.collection(u"atx").document(u'LED_R')
    doc = docs.get()

    if doc.exists:
        value = doc.to_dict()
        led.changeLed(int(value["R"]))

def getPow_G():
    docs = db.collection(u"atx").document(u'LED_G')
    doc = docs.get()

    if doc.exists:
        value = doc.to_dict()
        led.changeLed(int(value["G"]))

def getPow_B():
    docs = db.collection(u"atx").document(u'LED_B')
    doc = docs.get()

    if doc.exists:
        value = doc.to_dict()
        led.changeLed(int(value["B"]))

def initialize_firebase_app():
    global db
    if db is None:  # 이미 초기화되었는지 확인
        if not firebase_admin._apps:
            # Firebase 서비스 계정 키 파일의 경로
            cred = firebase_admin.credentials.Certificate("smart-planter-cde3d-firebase-adminsdk-4p05t-46a217b1d6.json")

            # Firebase 앱 초기화
            firebase_admin.initialize_app(cred, {
                'storageBucket': 'smart-planter-cde3d.appspot.com'
            })

            update()

        # Firebase 앱 가져오기
        db = firestore.client()
        doc_ref = db.collection(u'atx').document(u'power')
        doc_ref.on_snapshot(on_snapshot)
        callback_done.wait()


def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_dict = doc.to_dict()
        
        # R, G, B 값 변경 여부 확인
        if "R" in doc_dict:
            old_R = int(doc_dict["R"])
            # 변경된 값에 따라 changeLed 함수 호출
            led.changeLed_R(old_R)
        
        if "G" in doc_dict:
            old_G = int(doc_dict["G"])
            # 변경된 값에 따라 changeLed 함수 호출
            led.changeLed_G(old_G)
        
        if "B" in doc_dict:
            old_B = int(doc_dict["B"])
            # 변경된 값에 따라 changeLed 함수 호출
            led.changeLed_B(old_B)

    callback_done.set()

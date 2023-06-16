import firebase_admin
import threading
import lib.LedModule as led
import lib.bs as bs
from firebase_admin import credentials
from firebase_admin import firestore

db = None
callback_done = threading.Event()


def getPow_RGB():
    doc_R = db.collection(u"atx").document(u'LED_R')
    doc_G = db.collection(u"atx").document(u'LED_G')
    doc_B = db.collection(u"atx").document(u'LED_B')
    doc_L = db.collection(u"atx").document(u'LED')

    doc_R.on_snapshot(on_snapshot_R)
    doc_G.on_snapshot(on_snapshot_G)
    doc_B.on_snapshot(on_snapshot_B)
    doc_L.on_snapshot(on_snapshot_L)

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

        # Firebase 앱 가져오기
        db = firestore.client()
        getPow_RGB()
        callback_done.wait()

def on_snapshot_R(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_dict = doc.to_dict()
        
        if "R" in doc_dict:
            old_R = int(doc_dict["R"])
            led.changeLed_R(old_R)

def on_snapshot_G(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_dict = doc.to_dict()
        
        if "G" in doc_dict:
            old_G = int(doc_dict["G"])
            led.changeLed_G(old_G)

def on_snapshot_B(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_dict = doc.to_dict()
        
        if "B" in doc_dict:
            old_B = int(doc_dict["B"])
            led.changeLed_B(old_B)

def on_snapshot_L(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_dict = doc.to_dict()
        
        if "LED" in doc_dict:
            old_L = doc_dict["LED"]
            led.changeLed_L(old_L)


initialize_firebase_app()
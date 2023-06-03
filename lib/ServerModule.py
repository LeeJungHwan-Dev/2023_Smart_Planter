import firebase_admin
import threading
import lib.LedModule as led
from firebase_admin import credentials
from firebase_admin import firestore

db = None
callback_done = threading.Event()

def update():
    doc_ref = db.collection(u'led').document(u'power')
    doc_ref.update({u'init_pow': u'50'})

def getPow():
    docs = db.collection(u"led").document(u'power')
    doc = docs.get()

    if doc.exists:
        value = doc.to_dict()
        led.changeLed(int(value["pow"]))

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
        doc_ref = db.collection(u'led').document(u'power')
        doc_ref.on_snapshot(on_snapshot)
        callback_done.wait()


def on_snapshot(doc_snapshot, changes, read_time):
    #snapshot에서 name값 
    for doc in doc_snapshot:
        doc_dict = doc.to_dict()
        #pow 필드값이 존재할 경우 변경될 때마다 led 값 변경
        if "old_pow" in doc_dict:
            old_pow = int(doc_dict["old_pow"])  # int로 변환
            LedModule.changeLed(old_pow)

    callback_done.set()
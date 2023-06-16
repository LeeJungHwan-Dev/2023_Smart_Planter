import lib.LedModule as led
import lib.ServerModule as server
import firebase_admin
import time
from firebase_admin import credentials

# Firebase 서비스 계정 키 파일의 경로
cred = credentials.Certificate("smart-planter-cde3d-firebase-adminsdk-4p05t-46a217b1d6.json")

# Firebase 앱 초기화
firebase_admin.initialize_app(cred, {
    'storageBucket': 'smart-planter-cde3d.appspot.com'
})

server.initialize_firebase_app()

server.getPow_RGB()

while True:
    None

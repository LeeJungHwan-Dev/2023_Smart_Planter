#import lib.LedModule as led
import lib.ServerModule as server
import lib.UploadModule as upload
import firebase_admin
from firebase_admin import credentials

# Firebase 서비스 계정 키 파일의 경로
cred = credentials.Certificate("smart-planter-cde3d-firebase-adminsdk-4p05t-46a217b1d6.json")

# Firebase 앱 초기화
firebase_admin.initialize_app(cred, {
    'storageBucket': 'smart-planter-cde3d.appspot.com'
})

upload.initialize_firebase_app()
server.initialize_firebase_app()

#upload.upload_file("test.png","file.png")
server.update()
server.getPow()


while True:
    None
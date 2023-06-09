import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from datetime import datetime

# 스토리지 버킷 참조
bucket = None

# 파일 업로드
def upload_file(source_file, destination_blob_name):

    # 현재 날짜와 시간 가져오기
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S_")
    blob = bucket.blob(now_str+destination_blob_name)
    blob.upload_from_filename(source_file)

# 파일 다운로드
def download_file(source_blob_name, destination_file):
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file)

# 파일 삭제
def delete_file(blob_name):
    blob = bucket.blob(blob_name)
    blob.delete()

def initialize_firebase_app():
    global bucket
    if bucket is None:  # 이미 초기화되었는지 확인
        if not firebase_admin._apps:
            # Firebase 서비스 계정 키 파일의 경로
            cred = firebase_admin.credentials.Certificate("smart-planter-cde3d-firebase-adminsdk-4p05t-46a217b1d6.json")

            # Firebase 앱 초기화
            firebase_admin.initialize_app(cred, {
                'storageBucket': 'smart-planter-cde3d.appspot.com'
            })

        # Firebase 앱 가져오기
        bucket = storage.bucket()
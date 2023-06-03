import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

file_path = "1111.png"
upload_name = "file.png"

# Firebase 서비스 계정 키 파일의 경로
cred = credentials.Certificate("smart-planter-cde3d-firebase-adminsdk-4p05t-46a217b1d6.json")

# Firebase 앱 초기화
firebase_admin.initialize_app(cred, {
    'storageBucket': 'smart-planter-cde3d.appspot.com'
})

# 스토리지 버킷 참조
bucket = storage.bucket()

# 파일 업로드
def upload_file(source_file, destination_blob_name):
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file)

# 파일 다운로드
def download_file(source_blob_name, destination_file):
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file)

# 파일 삭제
def delete_file(blob_name):
    blob = bucket.blob(blob_name)
    blob.delete()

# 사용 예시
upload_file(file_path, upload_name)

# 비밀번호 걸어 압축하기 
# pip install pyminizip
import os
import pyminizip

folder = r'Cipher\0_resource'
file_toZip = 'test.txt'
zipped_name = 'abc.zip'
zip_path = os.path.join(folder, zipped_name)
pw = 'abc'

# 폴더 없으면 만들기
if not os.path.exists(folder):
    os.makedirs(folder)

# 압축하고 비번 설정
# (압축할 파일, 폴더 새로 안 만들고 그냥 압축, 경로+이름, 비번, 5레벨 압축)
# 0:최저 압축, 9:최고 압축
pyminizip.compress(file_toZip, None, zip_path, pw, 5)

print(f"압축성공(비번 abc): {file_toZip} -> {zip_path}")


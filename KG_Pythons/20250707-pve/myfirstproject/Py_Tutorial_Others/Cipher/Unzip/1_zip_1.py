# 압축하기 
import zipfile
import os

folder = r'Cipher\0_resource'
file_toZip = 'test.txt'
zipped_name = 'test1.zip'
zip_path = os.path.join(folder, zipped_name)

# 폴더가 없으면 만들기
if not os.path.exists(folder):
    os.makedirs(folder)

# 기본 코드
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write(file_toZip, os.path.basename(file_toZip))

print(f"{file_toZip} -> {zip_path}")



####[zip() 함수와 비교(= 리스트 묶기)]#####################
# #주의: zip() 함수는 zip 파일과 관련이 없음!!

# # 1. Packing: zip()
# a, b = ['a', 'b', 'c'], [1, 2, 3]

# for i in zip(a, b):
#     print(i)  # ('a', 1) ('b', 2) ('c', 3)
    
# for i in list(zip(a, b)):
#     print(i)  # ('a', 1) ('b', 2) ('c', 3)

# print(zip(a, b), list(zip(a, b)))
# # zip(a, b)은 interator의 주소: <zip object at 0x0000019BD3FE4980> 
# # list(zip())은 배열: [('a', 1), ('b', 2), ('c', 3)]

# # 자세한 수업은 Packaging에서 진행할 것.
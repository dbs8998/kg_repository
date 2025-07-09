# 2. txt파일: with open()만으로 IO 하기 

file_path = r'Cipher\0_resource\test_22.txt'

#1. 파일 생성
content = "엄마야 누나야 강변 살자."

# 'w'모드로 열어서 쓰고 저장하기.
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"파일 생성: {file_path}")

# #2. 파일 읽기
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
# print(f"파일내용: \n{content}")

# #3. 파일 업데이트
# addition = "\뜰에는 반짝이는 금모레빛"

# with open(file_path, 'a', encoding='utf-8') as file:
#     file.write(addition)

# print(f"파일내용: \n{file_path}")

# #4. 파일 삭제
import os

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"파일 {file_path}가 삭제됨")
else:
    print("파일이 존재하지 않습니다.")


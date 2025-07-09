# 1. txt파일: open() -> close() 한 쌍으로 IO 하기 

file_path = r'Cipher\0_resource\test_22.txt'

#1. 파일 생성
content = "엄마야 누나야 강변 살자."

# 'w'모드로 열어서 쓰고 저장하기.
file = open(file_path, "w", encoding='utf-8')
file.write(content)
file.close()
print(f"파일 생성: {file_path}")

# #2. 파일 읽기
# file = open(file_path, 'r', encoding='utf-8')
# txt_read = file.read()
# file.close()
# print(f"파일내용: \n{txt_read}")

# #3. 파일 업데이트
# addition = "\뜰에는 반짝이는 금모레빛"

# file = open(file_path, 'a', encoding='utf-8')
# file.write(addition)
# file.close()
# print(f"파일내용: \n{file_path}")

# #4. 파일 삭제
# import os

# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"파일 {file_path}가 삭제됨")
# else:
#     print("파일이 존재하지 않습니다.")

###########################################
## 종합
# import os

# # 파일 생성
# file_path = 'test_33.txt'
# content = 'Hello, this is a test file.'

# with open(file_path, 'w') as file:
#     file.write(content)

# print(f"파일 생성됨: {file_path}")

# # 파일 읽기
# with open(file_path, 'r') as file:
#     content = file.read()

# print(f"파일 내용:\n{content}")

# # 파일 업데이트 (내용 추가)
# additional_content = '\nThis is additional content.'

# with open(file_path, 'a') as file:  # 'a' 모드는 파일 끝에 내용을 추가
#     file.write(additional_content)

# print(f"파일 업데이트됨: {file_path}")

# # 파일 읽기 (업데이트 확인)
# with open(file_path, 'r') as file:
#     content = file.read()

# print(f"업데이트된 파일 내용:\n{content}")

# # 파일 삭제
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"파일 삭제됨: {file_path}")
# else:
#     print("파일이 존재하지 않습니다.")

# 기초지식: 0_ref_1.py
# pip install zipfile
import itertools
import zipfile

# abc -> def, azx -> dca
# 0~9: 48~57, A~z: 65~90, a~z: 97~122, 0~127: 아스키, 128~: 유니코드
# 주의: x = -1000일 때도 에러 안 나도록 할 것!
letters = []
for n in range(48, 58):
    letters.append(chr(n))
for m in range(65, 91):
    letters.append(chr(m))
for i in range(97, 123):
    letters.append(chr(i))
# print(letters)

zFile = zipfile.ZipFile(r"Cipher\0_resource\a12.zip")

# 부프트 포스 알고리즘으로 암호 해제 후 압축 풀기
unzipped_folder = r'Cipher\0_resource'
for len in range(1, 4): # Cartesian product
    combination = itertools.product(letters, repeat = len) # letters에서 꺼내서 len 길이로 조합
    for combi in combination:
        pw = ''.join(combi)
        # print(pw)
        try:
            zFile.extractall(path=unzipped_folder, pwd=pw.encode()) # pwd는 extractall의 인수
            print(f'비밀번호: {pw}')
            break
        except:
            pass

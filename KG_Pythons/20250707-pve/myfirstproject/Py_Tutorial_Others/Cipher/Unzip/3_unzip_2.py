# 기초지식: 0_ref_1.py
# pip install zipfile
import itertools
import zipfile

letters = []
for n in range(48, 58):
    letters.append(chr(n))
for m in range(65, 91):
    letters.append(chr(m))
for i in range(97, 123):
    letters.append(chr(i))

zFile = zipfile.ZipFile(r"Cipher\0_resource\a12.zip")  # 경로 변경
unzipped_folder = r'Cipher\0_resource'

found = False   # Flag를 지정함.
for length in range(1, 4):  # Cartesian product
    if found:
        break
    combination = itertools.product(letters, repeat=length)  # letters에서 꺼내서 len 길이로 조합
    for combi in combination:
        pw = ''.join(combi)
        try:
            zFile.extractall(path=unzipped_folder, pwd=pw.encode())  # pwd는 extractall의 인수
            print(f'비밀번호: {pw}')
            found = True     # Flag로 종료함
            break
        except:
            pass

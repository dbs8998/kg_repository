# Caeser cipher
# 알파벳에서 다음 3번째 글자로 변경: x = 3
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
print(letters)

op_choice = input("Enter 'en' or 'de' for encryption or decryption \n")
txt_in = input("Enter a text to encrypt: \n")
x = int(input("Enter a shift number: \n")) # 이동 자리수

# 1. 암호화 함수(parameter: txt_in, x)
def encrypt(txt_in, x):
    txt_encrypt = ""
    for letter in txt_in:
        # print(letter)
        pos_in_letters = letters.index(letter)
        posNew_in_letters = (pos_in_letters + x) % len(letters)
        letter_new = letters[posNew_in_letters]
        txt_encrypt += letter_new
    #print(txt_encrypt)
    return txt_encrypt
    
# res_encrypt = encrypt(txt_in, x)

# 2. 복호화 함수
def decrypt(txt_encrypt, y):
    txt_decrypt = ""
    for letter in txt_encrypt:
        pos_in_letters = letters.index(letter)
        posNew_in_letters = (pos_in_letters - y) % len(letters)
        if posNew_in_letters < 0:
            posNew_in_letters += len(letters)
        letter_new = letters[posNew_in_letters]
        txt_decrypt += letter_new
    # print(txt_decrypt)
    return txt_decrypt

# decrypt(res_encrypt, x)

# 3. 암호화/복호화 선택 실행 함수
def caeser_cipher(txt_in, x, op_choice):
    res = ""
    if op_choice == "en":
        res = encrypt(txt_in, x)
    elif op_choice == "de":
        res = decrypt(txt_in, x)
    # print(res)
    return res
print(caeser_cipher(txt_in, x, op_choice))


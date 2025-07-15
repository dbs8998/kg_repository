# class로 변환
class Cryption:
    def __init__(self):
        self.letters = []
        for l in range(48, 58): # 0~9
            self.letters.append(chr(l))
        for m in range(65, 91): # A~Z
            self.letters.append(chr(m))
        for n in range(97, 123): # a~z
            self.letters.append(chr(n))
        # print(self.letters)
    
    # 1. 암호화 함수(parameter: txt_in, x)
    def encrypt(self, txt_in, x):
        txt_encrypt = ""
        for letter in txt_in:
            # print(letter)
            pos_in_letters = self.letters.index(letter)
            posNew_in_letters = (pos_in_letters + x) % len(self.letters)
            letter_new = self.letters[posNew_in_letters]
            txt_encrypt += letter_new
        #print(txt_encrypt)
        return txt_encrypt
        
    # res_encrypt = encrypt(txt_in, x)

    # 2. 복호화 함수
    def decrypt(self, txt_in, x):
        txt_decrypt = ""
        for letter in txt_in:
            pos_in_letters = self.letters.index(letter)
            posNew_in_letters = (pos_in_letters - x) % len(self.letters)
            if posNew_in_letters < 0:
                posNew_in_letters += len(self.letters)
            letter_new = self.letters[posNew_in_letters]
            txt_decrypt += letter_new
        # print(txt_decrypt)
        return txt_decrypt

    # 3. 작업 실행
    def caeser_cipher(self):
        res = ""
        op_choice = input("Enter 'en' or 'de' for en-/deCryption \n")
        txt_in = input("Enter a text to encrypt: \n")
        x = int(input("Enter a shift number: \n")) # 이동 자리수
    
        if op_choice=="en":
            res = self.encrypt(txt_in, x)
        elif op_choice=="de":
            res = self.decrypt(txt_in, x)
        else:
            print("Invalid order.")
        return res

if __name__=="__main__":
    op_choice = input("Enter 'en' or 'de' for en-/deCryption \n")
    txt_in = input("Enter a text to encrypt: \n")
    x = int(input("Enter a shift number: \n")) # 이동 자리수
    cryption = Cryption()
    result = cryption.caeser_cipher(txt_in, x, op_choice)
    print(result)

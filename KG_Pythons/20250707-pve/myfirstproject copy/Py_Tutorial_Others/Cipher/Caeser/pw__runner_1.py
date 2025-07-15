from pw_encryption_2 import Cryption

txt_in = 'abc'
x = -3

cry = Cryption()
en1 = cry.encrypt(txt_in, x)
de1 = cry.decrypt(en1, x)
print(en1, " ", de1)

# choice = cry.caeser_cipher()
# print(choice)

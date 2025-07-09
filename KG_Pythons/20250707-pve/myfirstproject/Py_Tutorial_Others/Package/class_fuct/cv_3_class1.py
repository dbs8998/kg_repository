print('클래스파일(class1.py)이다.') # 전역 멤버는 남이 import만 해도 실행됨. 그걸 막으려면 함수로 만들거나 if문에 넣어야 함.
print(__name__) #__name__은 직접실행하면 __main__, 객체로 실행하면 class1임. 따라서 아래 if구문은 직접 실행할 때만 수행됨.

# > python cv_3_class1.py 또는 Ctrl+F5 로 직접 실행해보기.

####미션: 클래스 이해##################
## 1. 아래 변수와 함수만 클래스로 만들어서 다른 파일에서 호출하여 사용하기. 나머지는 그에 맞춰 변경 또는 유지.
## 2. if __name__ == '__main__': 으로 직접 실행할 때와 객체로 실행할 때의 동작을 다르게 만들기.

# a = 1
# def print_a(a):
#     print(a)
# def print_Cla1():
#     print("Class1")

# exit()

######################################

class Cla1:
    def __init__(self, a=1):
        self.a = a
    
    def print_a(self):
        print(self.a)
    
    def print_Cla1(self):
        print("Class1")

def cla1_funct(b):
    print(b)

if __name__ == '__main__':
    c1 = Cla1()
    c1.print_Cla1()

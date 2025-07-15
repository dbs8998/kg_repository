# abc는 클래스: abc.funct_1(), abc().funct_1()
# abc는 클래스 또는 함수: abc(funct_1()), abc(callback)

class Cla_1:
    @staticmethod
    def funct_1():  # 정적 메서드: 클래스 자체/객체 모두 호출 가능
        print("Cla_1 내의 funct_1 함수")

Cla_1.funct_1()   # 클래스 자체로 호출하는 경우
cla1 = Cla_1()
cla1.funct_1()    # 인스턴스로 호출하는 경우

class Cla_2:
    def funct_2(self):  # 인스턴스 메서드: 객체만 호출 가능
        print("Cla_2내 funct_2 함수")

cla2 = Cla_2()
cla2.funct_2()
# Cla_2.funct_2()  에러남. 인스턴스 메서드는 클래스로 직접 호출 안 됨.

def funct_3(x):
    print(f"funct_3 함수의 인자: {x}")
    
def funct_4():
    return "ddd의 리턴값"

funct_3(funct_4())

class Cla_3:
    def __init__(self, value):
        print(f"Cla_3 인스턴스의 인자값: {value}")

def funct_5():
    return "funct_5의 리턴값"

Cla_3(funct_5())


################################
# 억지로 만들어본 함수 abc의 abc().funct_1() 형태

def funct_5():
    class Cla_4:
        def funct_5_1(self):
            print("함수5 내의 클라4 내의 5_1 함수")
    return Cla_4()

funct_5().funct_5_1()

##################################

# abc(callback)에서 abc와 callback이 함수인 경우
def funct6(callback1):
    result = callback1()
    print(f"funct6 함수의 인자값: {result}")

def callback1():
    return "callback1의 리턴값"

funct6(callback1)

# abc(callback)에서 abc가 클래스인 경우
class Cla5:
    def __init__(self, callback2):
        result = callback2()
        print(f"Cla5 인스턴스의 인자값: {result}") 

def callback2():
    return "callback2의 리턴값"

cla5 = Cla5(callback2)

# abc(callback)에서 callback이 클래스인 경우
def funct7(cls):
    instance = cls()
    result = instance()
    print(f"funct7의 인자로 클래스를 받아 인스턴스를 생성함. 그 클래스의 인스턴스 함수를 호출한 리턴값: {result}")

class Callback:
    def __call__(self):  # 인스턴스를 함수처럼 호출하는 특수 메서드.
        return "Callback 클래스 내 인스턴스 함수의 리턴값"

funct7(Callback)

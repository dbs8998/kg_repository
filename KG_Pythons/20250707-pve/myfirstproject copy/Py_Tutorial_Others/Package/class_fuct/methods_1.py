# https://imdona.tistory.com/29 
# https://journeytosth.tistory.com/73
# 파이썬 메서드 3종: 클래스 메서드, 정적 메서드, 인스턴스 메서드 비교 (특수 메서드: __init__, __str__)
# 1. 인스턴스 메서드: method_instance(self)
### - 인스턴스 변수 사용
### - 클래스명.메소드명(인스턴스)
### - 인스턴스명.메소드명( )
### def method_inst(self)
# 2. 클래스 메서드: method_class(cls)
### - 클래스 변수 사용
### - 클래스명.메소드명()
### - 인스턴스명.메소드명()
### - 데코레이터로 선언해줘야 함(@classmethod)
### @classmethod #(데코레이터로 선언해줘야 함)
### def method_class(cls)
# 3. 정적 메서드
### - 인스턴스/클래스 변수 사용 않고 기능만 수행함
### - 클래스명.메소드명()
### - 인스턴스명. 메소드명()
### @staticmethod  #(데코레이터로 선언해줘야 함)
### method_static()

# 1. 인스턴스 메서드
class Inst:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self): # 인스턴스 변수 호출
        print(self.name, ", ", self.age)
    
    def test_func(self): # 인스턴스 메서드 호출
        self.print_info()

inst = Inst('hawx', 22)
# 인스턴스로 메서드 호출하기
inst.print_info()
inst.test_func()
# 억지: 클래스로 인스턴스를 호출하여 메서드 호출
Inst.test_func(inst)

# 2. 클래스 메서드
class UserCla:
    # 클래스 변수 정의
    count = 0
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        UserCla.count += 1
        
    def __str__(self):
        return f"사용자 이름: {self.name}, 이메일: {self.email}"
    
    # 클래스 메소드 : cls를 파라미터로 받음. 클래스 변수를 설정하거나 출력함.
    @classmethod
    def user_count(cls):
        print(f"총 유저 수: {cls.count}")

# User 인스턴스 생성
user1 = UserCla('김하나', '111@111.com', '1111')
user2 = UserCla('강이둘', '222@222.com', '2222')
user3 = UserCla('송삼식', '333@333.com', '3333')

# 클래스 메소드 사용하기
UserCla.user_count() # 총 유저 수: 3
user1.user_count()   # 총 유저 수: 3

# 3. 정적 메서드
class UserStatic:
    var_Cla = 0
    def __init__(self, name, email):
        self.name_Inst = name
        UserStatic.var_Cla += 1
    
    def __str__(self):
        return f"이름: {self.name_Inst}"
    
    @staticmethod
    def method_static(name, email):
        print(f'이름: {name}, 이메일: {email}')
        return "@" in email
    
user1 = UserStatic('이순신', '234@234.com')
user1.method_static('장일남', '333@333.com')
UserStatic.method_static('정이녀', '444@444.com')
print(user1.method_static('ggg', '444@444.com'))
print(UserStatic.method_static('rrr', '777@777.com'))


#########################
# # 통합
# class User:
#     # 클래스 변수 정의
#     count = 0

#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#         User.count += 1

#     def __str__(self):
#         return f"사용자 이름 : {self.name}, 이메일 : {self.email}"

#     # 클래스 메소드 : 클래스를 파리미터로 받는 클래스 메소드, 클래스 변수의 값을 설정하거나 출력
#     @classmethod
#     def number_of_users(cls):
#         print(f"총 유저수는 {cls.count}입니다.")

#     # 정적 메소드 : 기능적인 역할만 한다, 인스턴스 변수나 클래스 변수 둘 다 사용하지 않을 때
#     @staticmethod
#     def is_valid_email(email):
#         '''파라미터로 받은 email에 @이 들어있는지 확인'''
#         return "@" in email

# # User 클래스의 인스턴스 생성
# user1 = User('dona', 'iminj1995@gmail.com', '1234')
# user2 = User('salmon', 'salmon@gmail.com', '3456')
# user3 = User('lee_king_hee', 'kayyounghl@gmail.com', '5678')
# user4 = User('teco', 'teco@gmail.com', '6789')

# # 클래스 메소드 사용하기
# # {클래스 이름}.{메소드 이름}( ), {인스턴스 이름}.{메소드 이름}( ) 두 방법 모두 가능
# User.number_of_users() # out : 총 유저수는 4입니다.
# user1.number_of_users() # out : 총 유저수는 4입니다.

# # 정적메소드 사용하기 : 클래스 인스턴스 모두 사용 가능
# print(User.is_valid_email('hello')) # out : False
# print(user1.is_valid_email('hello@tistory.com')) # out : True

###################################
# 대표적 특수 메서드: __init__(), __str__()


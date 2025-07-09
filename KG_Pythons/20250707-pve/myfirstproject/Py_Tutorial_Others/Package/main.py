##Step 1: 
# (a) __init__.py 없는 경우
import package_noInit.module1
import package_noInit.module2
import package_noInit.subpackage.submodule

print(package_noInit.module1.m1())
print(package_noInit.module2.m2())
print(package_noInit.subpackage.submodule.sub_m1())

# # No init: module1의 m1 함수임.
# # No init: module2의 m2 함수임.
# # No init: submodule의 sub_m1 함수.

# # (b) __init__.py 있는 경우
# import package_init

# print(package_init.module1.m1())
# print(package_init.module2.m2())
# print(package_init.subpackage.submodule.sub_m1())

# # subpackage를 불러왔음.
# # package_init을 불러왔습니다.
# # module1의 m1 함수임.
# # module2의 m2 함수임.
# # submodule의 sub_m1 함수.

# # Step 2: Logger 적용
# import package_init

# print(package_init.module1.m1())
# print(package_init.module2.m2())
# print(package_init.subpackage.submodule.sub_m1())

# # 2024-06-07 10:12:29,450 - package_init - INFO - package_init logger를 불러왔음.
# # subpackage __init__을 불러왔음.
# # 2024-06-07 10:12:29,452 - package_init.subpackage - INFO - subpackage_init logger를 불 러왔음.
# # module1의 m1 함수임.
# # module2의 m2 함수임.
# # submodule의 sub_m1 함수.

# # Step 3: Config 적용
# import package_init

# print(package_init.module1.m1())
# print(package_init.module2.m2())
# print(package_init.subpackage.submodule.sub_m1())

# # subpackage __init__을 불러왔음.
# # module1의 m1 함수임. 설정값: value1
# # module2의 m2 함수임. 설정값: value2
# # submodule의 sub_m1 함수. 설정: value1

# # Step 4: Config 별도 파일 + Log
# import package_init_config
# import package_init_config.module1
# import package_init_config.module2
# import package_init_config.subpackage

# print(package_init_config.module1.m1())
# print(package_init_config.module2.m2())
# print(package_init_config.subpackage.submodule.sub_m1())

# # 2024-06-07 11:11:52,004 - package_init_config - INFO - package_init logger를 불러왔음.
# # subpackage __init__을 불러왔음.
# # 2024-06-07 11:11:52,010 - package_init_config.subpackage - INFO - subpackage_init logger를 불러왔음.
# # module1의 m1 함수임. 설정값: value1
# # module2의 m2 함수임. 설정값: value2
# # submodule의 sub_m1 함수. 설정: value1

# # Step 5: Logging + Config 한 파일
# import package_init_config

# print(package_init_config.module1.m1())
# print(package_init_config.module2.m2())
# print(package_init_config.subpackage.submodule.sub_m1())

# # 2024-06-07 11:36:37,184 - package_init_config - INFO - package_init logger를 불러왔음.
# # subpackage __init__을 불러왔음.
# # 2024-06-07 11:36:37,188 - package_init_config.subpackage - INFO - subpackage_init logger를 불러왔음.
# # module1의 m1 함수임. 설정값: value1
# # module2의 m2 함수임. 설정값: value2
# # submodule의 sub_m1 함수. 설정: value1

# # Step 6~7: Class 적용
# import package_init_config.module1
# from package_init_config import module2
# import package_init_config.subpackage.submodule as sm

# # Module1, Module2, Submodule 클래스 인스턴스 생성(대소문자 구분)
# M1 = package_init_config.module1.Module1()
# M2 = module2.Module2()
# SM = sm.Submodule()

# # 인스턴스 매서드 호출
# print(M1.m1())
# print(M2.m2())
# print(SM.sub_m1())

#####################################################
'''멤버 import
# 1. 패키지 = 폴더
import package_init_config  # package_init_config는 패키지

# 2. 모듈 = 파일
import package_init_config.module1  # package_init_config/module1.py는 모듈
from package_init_config import module2 # package_init_config/module2.py는 모듈

# 3. 클래스
from package_init_config.module1 import Module1  # Module1은 클래스

# 4. 함수 (모듈 멤버)
from package_init_config.module1 import m1  # m1은 함수: 모듈에 속하나 클래스에 속하면 안 됨. 클래스 멤버는 클래스를 인스턴스화 하고 나서 호출해야 함.

# 5. 함수 (클래스 멤버)
# 클래스 import
from my_package.module1 import Module1
# 클래스 인스턴스 생성
module1_instance = Module1()
# 클래스 인스턴스를 통해 메서드 호출
print(module1_instance.m1())  # "module1의 m1 함수, 설정: value1"
print(module1_instance.sum_int_vars())  # "module1의 합: 30"

'''
#####################################################

# # 2024-06-07 14:13:10,101 - package_init_config - INFO - package_init logger를 불러왔음.
# # subpackage __init__을 불러왔음.
# # 2024-06-07 14:13:10,103 - package_init_config.subpackage - INFO - subpackage_init logger를 불러왔음.
# # module1의 m1 함수임. 설정값: value1
# # module2의 m2 함수임. 설정값: value2
# # submodule의 sub_m1 함수. 설정: value1

# # 2024-06-07 14:46:28,944/package_init_config/INFO : package_init logger를 불러왔음.
# # subpackage __init__을 불러왔음.
# # 2024-06-07 14:46:28,948/package_init_config.subpackage/INFO : subpackage_init logger를 불러왔음.
# # module1의 m1 함수임. 설정값: value1. 합: 30
# # module2의 m2 함수임. 설정값: value2. 합: 30
# # submodule의 sub_m1 함수. 설정: value1

# 패키지 초기화 코드
# - 패키지 내 모듈과 하위 패키지를 미리 import하여 편리하게 접근하게 해줌.
# - 패키지 내 전역변수, 설정값을 초기화함. (이 부분은 )
# - 패키지 내 로깅 설정을 함.

##################################################
# Step 1: 기본 구조
# 하위 모듈 및 패키지 포함
from . import module1
from . import module2
from .subpackage import submodule

print("package_init을 불러왔습니다.")

#####################################################
# # Step 2: Log 적용
# # 로깅 설정
# import logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
# logger.info("package_init logger를 불러왔음.")

# # 하위 모듈 및 패키지 포함
# from . import module1
# from . import module2
# from .subpackage import submodule

###################################################
# # Step 3: Config 적용

# # 초기 설정
# CONFIG = {
#     'setting1':'value1',
#     'setting2':'value2'
# }

# # 하위 모듈 및 패키지 포함
# from . import module1
# from . import module2
# from .subpackage import submodule

###################################################
# Step 4: 미션
# Logging + Config 별도 파일로 만들기 + 전역변수 지정하기

###################################################
# Step 5: 미션
# Class 적용하기.

###################################################
# # Step 6: 미션 (__init__()과 비교하기. class에 대해 배운 후 진행)
# # 모듈을 Class로 만들어 불러와보시오. (package, class, module, function 구분하기)

###################################################
# Step 7: 미션 
# __init__.py에 정수형 전역변수 2개를 정의하고 각 모듈에서 그 수를 계산한 값을 출력하라.

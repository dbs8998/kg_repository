###################################################
# # Step 4: 미션
# # Logging + Config 별도 파일로 만들기

# import logging

# # 로깅 설정
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
# logger.info("package_init logger를 불러왔음.")

# # 하위 모듈 및 패키지 포함
# from . import module1
# from . import module2
# from .subpackage import submodule

###################################################
# # Step 5: 미션
# # Logging + Config 한 __init__.py 파일로 만들기

# import logging

# # 초기 설정: get_config() 함수로 불어 쓸 수 있게 해주는 것이 핵심
# CONFIG = {
#     'setting1': 'value1',
#     'setting2': 'value2'
# }

# def get_config():
#     return CONFIG

# # 로깅 설정
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
# logger.info("package_init logger를 불러왔음.")

# # 하위 모듈 및 패키지 포함
# from . import module1
# from . import module2
# from .subpackage import submodule

###################################################
# # Step 6: 미션 (__init__()과 비교하기. class에 대해 배운 후 진행)
# # 모듈을 Class로 만들어 불러와보시오. (package, class, module 구분하기)

# import logging

# # 초기 설정
# CONFIG = {
#     'setting1': 'value1',
#     'setting2': 'value2'
# }

# def get_config():
#     return CONFIG

# # 로깅 설정
# logging.basicConfig(level=logging.INFO, format='%(asctime)s/%(name)s/%(levelname)s : %(message)s')
# logger = logging.getLogger(__name__)
# logger.info("package_init logger를 불러왔음.")

# # 하위 모듈 및 패키지 포함
# from . import module1
# from . import module2
# from .subpackage import submodule

###################################################
# Step 7: 미션 
# __init__.py에 정수형 전역변수 2개를 정의하고 각 모듈에서 그 수를 계산한 값을 출력하라.

import logging

# 초기 설정
CONFIG = {
    'setting1': 'value1',
    'setting2': 'value2'
}

# 정수형 전역변수
num1 = 10
num2 = 20

def get_config():
    return CONFIG

def get_nums():
    return num1, num2

# Logging 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s/%(name)s/%(levelname)s : %(message)s')
logger = logging.getLogger(__name__)
logger.info("package_init logger를 불러왔음.")

# 하위 모듈 및 패키지 포함
from . import module1
from . import module2
from .subpackage import submodule



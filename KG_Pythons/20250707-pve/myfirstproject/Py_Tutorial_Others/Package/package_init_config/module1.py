# # Step 4: .config에서 import 해줘야 함.
# from .config import CONFIG

# def m1():
#     return f"module1의 m1 함수임. 설정값: {CONFIG['setting1']}"

# # Step 5: getter로 불러오기
# from . import get_config

# def m1():
#     CONFIG = get_config()
#     return f"module1의 m1 함수임. 설정값: {CONFIG['setting1']}"

# Step 6: Class 적용
from . import get_config, get_nums

class Module1:
    def __init__(self):
        self.config = get_config()
        self.num1, self.num2 = get_nums()
        
    def m1(self):
        return f"module1의 m1 함수임. 설정값: {self.config['setting1']}. 합: {self.num1 + self.num2}"
    
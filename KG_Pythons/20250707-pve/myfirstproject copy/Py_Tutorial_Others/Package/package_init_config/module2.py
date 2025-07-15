# # Step 4: .config에서 import 해줘야 함.
# from .config import CONFIG

# def m2():
#     return f"module2의 m2 함수임. 설정값: {CONFIG['setting2']}"
    
# # Step 5: getter로 불러오기
# from . import get_config

# def m2():
#     CONFIG = get_config()
#     return f"module2의 m2 함수임. 설정값: {CONFIG['setting2']}"

# Step 6: Class 적용
from . import get_config, get_nums

class Module2:
    def __init__(self):
        self.config = get_config()
        self.num1, self.num2 = get_nums()
        
    def m2(self):
        return f"module2의 m2 함수임. 설정값: {self.config['setting2']}. 합: {self.num1+self.num2}"
    
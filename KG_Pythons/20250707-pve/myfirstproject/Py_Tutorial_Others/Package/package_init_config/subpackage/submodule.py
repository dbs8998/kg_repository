# # Step 4
# from ..config import CONFIG

# def sub_m1():
#     return f"submodule의 sub_m1 함수. 설정: {CONFIG['setting1']}"

# # Step 5: getter로 불러오기
# from .. import get_config

# def sub_m1():
#     CONFIG = get_config()
#     return f"submodule의 sub_m1 함수. 설정: {CONFIG['setting1']}"
    
# Step 6: Class 적용
from .. import get_config
class Submodule:
    def __init__(self):
        self.config = get_config()
        
    def sub_m1(self):
        return f"submodule의 sub_m1 함수. 설정: {self.config['setting1']}"
    
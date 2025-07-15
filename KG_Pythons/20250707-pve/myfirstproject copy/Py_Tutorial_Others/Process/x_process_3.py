import subprocess

# 외부 프로그램 실행
result = subprocess.run(['cmd', '/c', 'dir'], capture_output=True, text=True)
print(result.stdout)


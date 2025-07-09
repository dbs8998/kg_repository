import subprocess

# 자식 프로세스 실행 명령어
child_command = ["python", "-c", "print('자식 프로세스')"]

# 자식 프로세스 실행
child_process = subprocess.Popen(child_command)

# 부모 프로세스가 하려던 작업
print('부모 프로세스')

# 자식 프로세스가 종료될 때까지 대기
child_process.wait()
print('자식 프로세스가 종료되었습니다.')

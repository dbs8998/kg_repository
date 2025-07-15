import subprocess

# 자식 프로세스 실행 명령어
child_command = ["dir"]

# 자식 프로세스 실행
child_process = subprocess.Popen(child_command, shell=True)

# 부모 프로세스 작업
print('부모 프로세스')

# 자식 프로세스가 종료될 때까지 대기
child_process.wait()

# 자식 프로세스 종료 후 메시지 출력
print('자식 프로세스가 종료되었습니다.')

# daemon, join() 사용하여 쓰레드 종료 조건 설정하기

import threading

def math(threadName, value):
    sum = 0
    for i in range(0, value):
        sum += i
        print (f"{threadName}: {sum}")

th1 = threading.Thread(target=math, args=("쓰레드 1", 10))    
th2 = threading.Thread(target=math, args=('쓰레드 2', 10))

th1.daemon = True # 데몬 쓰레드(메인이 종료되면 같이 중단됨). 단, 쓰레드 스케줄링 때문에 이미 실행 시간을 할당받은 쓰레드 작업은 진행되고 중단됨.

th1.start()
th2.start()

print("메인 쓰레드는 한 번만 구동해봄.")

# 특정 쓰레드 종료까지 메인 쓰레드 종료 대기
# th1.join() # th1이 종료될 때까지 메인이 기다렸다 함께 종료됨. 활성화하면 daemon 때문에 중단되었던 쓰레드 1이 끝까지 실행됨.


# 함수 하나로 두 thread 동작 수행하기

import threading

def math(threadName, value):
    sum = 0
    for i in range(0, value):
        sum += i
        print (f"{threadName}: {sum}")

th1 = threading.Thread(target=math, args=("쓰레드 1", 10))    
th2 = threading.Thread(target=math, args=('쓰레드 2', 10))

th1.start()
th2.start()

print("메인 쓰레드는 한 번만 구동해봄.")

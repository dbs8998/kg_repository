# Thread로 두 동작 동시 수행하기
import threading
import time

def funct():
    while True:
        print("쓰레드 1")
        time.sleep(1.0)

th1 = threading.Thread(target=funct)
th1.start()

while True:
    print("메인 쓰레드")
    time.sleep(2.0)
    
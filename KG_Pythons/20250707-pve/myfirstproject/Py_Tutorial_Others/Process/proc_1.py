import multiprocessing

# 프로세싱 대상 함수
def task(process_name):
    cnt=0
    for _ in range(100):
        print(process_name, cnt)
        cnt += 1

if __name__=="__main__":
    #프로세스 생성
    process1= multiprocessing.Process(target=task, args=("프로세스1",))
    process2= multiprocessing.Process(target=task, args=("프로세스2",))

    #프로세스 시작
    process1.start()
    process2.start()
   
    # #메인 프로세스가 종료될 때까지 대기
    # process1.join()
    # process2.join()

    # # 메인 종료 시 2도 종료
    # process2.daemon = True
    
# 미션 1단계: 파일 3개를 읽고 파일별로 특정 단어의 출현 빈도를 집계하여 출력하시오. 위 작업을 파일별로 동시에 수행하시오.
# 미션 2단계: 각 빈도의 총합을 출력하시오.

import threading

# 파일 내에서 단어의 출현 빈도를 계산하는 함수
def word_frequency(file_name, word):
    try:
        # 파일 열기
        with open(file_name, 'r', encoding='utf-8') as file:
            # 파일 내용 읽기
            content = file.read()
            # 단어 빈도 계산
            frequency = content.count(word)
            # 결과 출력
            print(f"{file_name}에서 '{word}' 사용빈도: {frequency}회")
    except FileNotFoundError:
        print(f"{file_name} 파일이 없습니다.")

# 파일별 처리
def process_files(files, word):
    freq_sum = 0
    # 파일별 쓰레드 생성
    threads = []
    for file in files:
        thread = threading.Thread(target=word_frequency, args=(file, word))
        threads.append(thread)
        thread.start()

    # 모든 쓰레드가 집계를 종료할 때까지 메인 중지
    for thread in threads:
        thread.join()
    
# 메인 함수
def main():
    # 파일 목록
    files = ['Thread/file1.txt', 'Thread/file2.txt', 'Thread/file3.txt']
    # 찾을 단어
    word = '사과'
    # 집계 실행
    process_files(files, word)

if __name__=="__main__":
    main()


#############################
# 미션 2: 빈도 총합 출력 (Queue를 이용한 방법)

'''
import threading
import queue

# 파일에서 단어의 출현 빈도를 계산하는 함수
def word_frequency(file_name, word, q):
    try:
        # 파일 열기 (UTF-8로 인코딩 설정)
        with open(file_name, 'r', encoding='utf-8') as file:
            # 파일 내용 읽기
            content = file.read()
            # 단어의 출현 빈도 계산
            frequency = content.count(word)
            # 결과 출력
            print(f"{file_name}에서 '{word}' 사용빈도: {frequency}회")
            # 결과를 큐에 넣기
            q.put(frequency)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
        q.put(0)

# 각 파일에서 단어의 출현 빈도를 계산하고 총합을 출력하는 함수
def process_files(files, word):
    total_frequency = 0
    q = queue.Queue()

    # 각 파일에 대해 스레드 생성
    threads = []
    for file in files:
        thread = threading.Thread(target=word_frequency, args=(file, word, q))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 종료될 때까지 기다림
    for thread in threads:
        thread.join()

    # 큐에서 결과를 가져와서 총합 계산
    while not q.empty():
        total_frequency += q.get()

    print(f"모든 파일에서 '{word}'의 총 사용빈도: {total_frequency}회")

# 메인 함수
def main():
    # 파일 목록
    files = ["Thread/file1.txt", "Thread/file2.txt", "Thread/file3.txt"]
    # 찾고자 하는 단어
    word = "사과"
    # 파일에서 단어의 출현 빈도 계산 및 총합 출력
    process_files(files, word)

if __name__ == "__main__":
    main()

'''

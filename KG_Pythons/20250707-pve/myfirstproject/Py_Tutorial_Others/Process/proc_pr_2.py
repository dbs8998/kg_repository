# 멀티쓰레드와 멀티프로세스를 동시에 활용하는 코드
# 미션: 멀티쓰레드를 사용하여 센서 데이터를 수집하고, 멀티프로세스를 사용하여 데이터를 병렬로 처리하는 간단한 IoT 시뮬레이션 시스템을 구현해보기.

import threading
import multiprocessing
import time
import random
import queue

# 센서 데이터 수집 함수
def read_sensor(sensor_type, sensor_id, data_queue):
    while True:
        value = random.uniform(0.0, 100.0) # 가상 데이터 생성
        data_queue.put((sensor_type, sensor_id, value))
        time.sleep(1) # 1초마다 데이터 수집

# 데이터 처리 함수
def process_data(data):
    sensor_type, sensor_id, value = data
    print(f"센서 ID: {sensor_id}, 종류: {sensor_type}, 값: {value}")
    # 여기서 데이터를 실제로 처리하는 코드 작성
    time.sleep(2) # 데이터 처리 시뮬레이션
    
def sensor_thread(data_queue):
    pass

'''
import threading
import multiprocessing
import time
import random
import queue

# 센서 데이터 수집 함수
def read_sensor(sensor_type, sensor_id, data_queue):
    while True:
        value = random.uniform(0.0, 100.0)  # 가상 데이터 생성
        data_queue.put((sensor_type, sensor_id, value))
        time.sleep(1)  # 1초마다 데이터 수집

# 데이터 처리 함수
def process_data(data):
    sensor_type, sensor_id, value = data
    print(f"Processing data from Sensor ID: {sensor_id}, Type: {sensor_type}, Value: {value}")
    # 여기서 데이터를 실제로 처리하는 코드 작성
    time.sleep(2)  # 데이터 처리 시뮬레이션

def sensor_thread(data_queue):
    # 센서 목록 정의
    sensors = [("temperature", 1), ("humidity", 2), ("light", 3)]

    threads = []
    for sensor_type, sensor_id in sensors:
        thread = threading.Thread(target=read_sensor, args=(sensor_type, sensor_id, data_queue))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # 스레드들이 실행되도록 유지
    for thread in threads:
        thread.join()

def main():
    data_queue = queue.Queue()
    processed_queue = multiprocessing.Queue()

    # 센서 데이터 수집 스레드 시작
    sensor_thread_instance = threading.Thread(target=sensor_thread, args=(data_queue,))
    sensor_thread_instance.daemon = True
    sensor_thread_instance.start()

    # 데이터 처리 프로세스 시작
    while True:
        if not data_queue.empty():
            data = data_queue.get()
            process_instance = multiprocessing.Process(target=process_data, args=(data,))
            process_instance.start()
            process_instance.join()

        time.sleep(1)  # 메인 루프 주기

if __name__ == "__main__":
    main()
'''
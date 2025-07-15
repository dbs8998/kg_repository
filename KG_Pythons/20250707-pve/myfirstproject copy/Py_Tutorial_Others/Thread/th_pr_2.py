# 미션3: IoT 구현 -> 추후에 소켓으로 데이터 전송하기 추가할 것.
# 서브미션: 실제 센서를 연결하여 쓰레드로 처리해볼 것.

import threading
import time
import random
import queue

# 센서 데이터 수집 함수
def read_temperature(sensor_id, data_queue):
    while True:
        temperature = random.uniform(15.0, 25.0) #15.0~25.0 가상 데이터 생성
        data_queue.put(('temperature', sensor_id, temperature))
        time.sleep(1)  # 1초마다 데이터 수집

# random.random() : 0.0 ~ 1.0 부동 소수점(float)
# random.randint(a, b): a ~ b 정수
# random.uniform(a, b): a ~ b float

def read_humidity(sensor_id, data_queue):
    while True:
        humidity = random.uniform(30.0, 70.0)  # 가상 데이터 생성
        data_queue.put(('humidity', sensor_id, humidity))
        time.sleep(1)  # 1초마다 데이터 수집

def read_light(sensor_id, data_queue):
    while True:
        light = random.uniform(100, 1000)  # 가상 데이터 생성
        data_queue.put(('light', sensor_id, light))
        time.sleep(1)  # 1초마다 데이터 수집

# 데이터 처리 함수
def process_data(data_queue):
    while True:
        while not data_queue.empty():
            sensor_type, sensor_id, value = data_queue.get()
            print(f"Sensor ID: {sensor_id}, Type: {sensor_type}, Value: {value}")
        time.sleep(1)  # 1초마다 데이터 처리

def main():
    data_queue = queue.Queue()

    # 각 센서 스레드 생성
    temperature_thread = threading.Thread(target=read_temperature, args=(1, data_queue))
    humidity_thread = threading.Thread(target=read_humidity, args=(2, data_queue))
    light_thread = threading.Thread(target=read_light, args=(3, data_queue))

    # 데이터 처리 스레드 생성
    processing_thread = threading.Thread(target=process_data, args=(data_queue,))

    # 데몬 스레드로 설정하여 메인 스레드 종료 시 함께 종료되도록 설정
    temperature_thread.daemon = True
    humidity_thread.daemon = True
    light_thread.daemon = True
    processing_thread.daemon = True

    # 스레드 시작
    temperature_thread.start()
    humidity_thread.start()
    light_thread.start()
    processing_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  # Ctrl+C
        print("프로그램 종료")

if __name__ == "__main__":
    main()

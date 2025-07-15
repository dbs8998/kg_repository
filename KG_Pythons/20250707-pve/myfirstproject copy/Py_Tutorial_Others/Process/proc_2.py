import multiprocessing

# 숫자 배열처리 함수
def processing_nums(nums):
    squared_nums = [n ** 2 for n in nums]
    print(f"제곱수: {squared_nums}")

def main():
    num_list = [1,2,3,4,5,6,7,8,9,10]

    # 멀티스레드로 배열처리
    process_count = 4    # 사용할 프로세스 계수
    chunk_size = len(num_list) // process_count
    processes = []

    for i in range(process_count):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != process_count - 1 else len(num_list)
        process = multiprocessing.Process(target=processing_nums, args=(num_list[start_index:end_index],))
        processes.append(process)
        process.start()
        
    # 모든 프로세스가 종료될 때까지 대기
    for process in processes:
        process.join()

if __name__=="__main__":
    main()

        
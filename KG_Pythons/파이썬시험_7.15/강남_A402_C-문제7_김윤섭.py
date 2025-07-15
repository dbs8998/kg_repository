import numpy as np

#크기가 10*10 2차원 배열 생성
arr = np.arange(100).reshape(10,10)

print(arr)

#0으로 초기화
zeros = np.zeros(arr.shape)

#대각선 요소를 1로 변경(X모양)
# np.fill_diagonal(zeros, 1)

for i in range(zeros.shape[0]):
    zeros[i,i] = 1
    zeros[i, ((zeros.shape[0]-1) - i)] = 1

print(zeros)

#배열의 각 행과 열의 합 
print('각 행의 합 :', np.sum(arr, axis=1))
print('각 열의 합 :', np.sum(arr, axis=0))

#배열의 전체평균 표준편차
print('전체 평균 :', np.mean(arr))
print('표준 편차 :', np.std(arr))

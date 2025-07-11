# numpy와 matplotlib으로 임의의 이미지 데이터를 생성하고, 서브플롯에서 다양한 매개변수로 이미지를 다르게 렌더링함.

import numpy as np
import matplotlib.pyplot as plt

# 임의의 5x5 이미지 데이터 생성
data = np.random.random((5, 5))

# X: 이미지 데이터
plt.subplot(2, 4, 1)
plt.imshow(data)
plt.title('X: Image Data')

# cmap (컬러 맵): 'viridis'
plt.subplot(2, 4, 2)
plt.imshow(data, cmap='viridis')
plt.title('cmap: Viridis')

# interpolation (보간법): 'bicubic'
plt.subplot(2, 4, 3)
plt.imshow(data, interpolation='bicubic')
plt.title('Interpolation: Bicubic')

# aspect (가로세로 비율): 'equal'
plt.subplot(2, 4, 4)
plt.imshow(data, aspect='equal')
plt.title('Aspect: Equal')

# extent: 좌표 범위 지정
plt.subplot(2, 4, 5)
plt.imshow(data, extent=[-2, 2, -2, 2])
plt.title('Extent: [-2, 2, -2, 2]')

# vmin, vmax: 컬러 맵 범위 지정
plt.subplot(2, 4, 6)
plt.imshow(data, vmin=0.2, vmax=0.8)
plt.title('vmin=0.2, vmax=0.8')

# origin: 이미지 원점 위치
plt.subplot(2, 4, 7)
plt.imshow(data, origin='lower')
plt.title('Origin: Lower')

# 그 외 다양한 매개변수 활용
plt.subplot(2, 4, 8)
plt.imshow(data, alpha=0.5, cmap='hot', interpolation='nearest')
plt.title('Other Parameters')

plt.show()

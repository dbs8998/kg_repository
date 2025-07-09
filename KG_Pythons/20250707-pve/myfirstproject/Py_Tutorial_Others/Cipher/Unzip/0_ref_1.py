# 조합함수(데카르트곱): 
# itertoos.product(*iterables, repeat=1)
# 반환값: 조합 iterator

import itertools

# 예 1: 두 리스트의 데카르트곱
result = itertools.product([1, 2], ['a', 'b'])

for item in result:
    print(item)

# 출력
# (1, 'a')
# (1, 'b')
# (2, 'a')
# (2, 'b')

# 예 2: 한 개 리스트에 repeat를 걸어 한 데카르트곱
result = itertools.product([1, 2], repeat=2)

for item in result:
    print(item)

# # 출력
# (1, 1)
# (1, 2)
# (2, 1)
# (2, 2)

# "".join()
# 문자만 됨. 
a = ",".join(["a", "b", "c"])
print(a)   # a,b,c

# # 숫자 안 됨.
# a = ''.join([1, 2, 3])   # 에러남. str이 없음

# 미션 1: 아래 두 개 이상의 매개변수에 대한 가능한 모든 조합을 출력하고 합친(join()) 값도 출력하시오.

# import itertools
colors = ['red', 'green']
sizes = ['S', 'M', 'L']

combinations = itertools.product(colors, sizes)

for combi in combinations:
    print(combi)
    x = ''.join(combi)
    print(x)

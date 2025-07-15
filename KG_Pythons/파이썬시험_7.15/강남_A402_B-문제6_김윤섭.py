import random

random_int = []
for i in range(30):
   random_int.append(random.randint(1,9))


try:
    print('리스트 : ', random_int)

    random_int.sort()

    #딕셔너리를 이용한 중복횟수 체크
    dic = {}
    for i in random_int:
        if dic.get(i) == None:
            dic[i] = 1
        else:
            dic[i] = dic.get(i) + 1

    print(dic)

    #중복횟수
    max_val = max(dic.values())
    #가장많이 나온 수 - 여러개 나올수있으므로 list
    max_ints = []

    for k,v in dic.items():
        if v == max_val:
            max_ints.append(k)

    print(f'중복 횟수가 가장 많은 수 {max_ints}, 중복횟수 {max_val}')


except Exception as e:
    print('Exception : ', e)
#주의: zip() 함수는 zip 파일과 관련이 없음!!
# zip() = Packing, zip(*) = Unpacking

####[패킹]##########################################
# 1. Packing: zip()
a, b = ['a', 'b', 'c'], [1, 2, 3]

for i in zip(a, b):
    print(i)  # ('a', 1) ('b', 2) ('c', 3)
    
for i in list(zip(a, b)):
    print(i)  # ('a', 1) ('b', 2) ('c', 3)

#위의 결과는 같지만 실상 print해보면 다름
print(zip(a, b), list(zip(a, b)))
# zip(a, b)은 interator의 주소: <zip object at 0x0000019BD3FE4980> 
# list(zip())은 배열: [('a', 1), ('b', 2), ('c', 3)]


# # 예제 1: 아래 리스트의 원형을 만들고 for 문으로 아래 리스트를 출력하라.
# # [('Alice', 85), ('Bob', 90), ('Charlie', 88)]

## [풀이]
# # 두 개의 리스트를 정의합니다. 
# # (다음 장에서 언패킹 연산자로 푸는 법을 배우지만 일단 이렇게 진행함)
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 88]

# # zip()을 사용하여 두 개의 리스트를 묶습니다.
# zipped = zip(names, scores)

# # 결과를 리스트로 변환하여 출력합니다.
# zipped_list = list(zipped)
# print(zipped_list)


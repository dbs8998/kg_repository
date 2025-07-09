# ####[언패킹으로 가독성을 높여보자]##################
# * 연산자는 리스트나 튜플을 언패킹하여 변수에 할당하거나 함수 인자로 전달함.
# ** 연산자는 딕셔너리를 언패킹하여 키워드 인자로 전달할 때 사용됨.
#####################################################

# zip(*) = Unpacking: "*"은 언패킹 연산자
# 예: zip()으로 묶인 리스트
zipped_list = [('Alice', 85), ('Bob', 90), ('Charlie', 88)]

# *를 사용하여 언패킹을 수행
names_unzipped, scores_unzipped = zip(*zipped_list)

# 결과를 출력
print(names_unzipped)  # ('Alice', 'Bob', 'Charlie')
print(scores_unzipped) # (85, 90, 88)
####################################################

# 1. 일반적인 언패킹: 리스트, 튜플
numbers = [1, 2, 3]
a, b, c = numbers

print(a, b, c)  # 1, 2, 3

# 2. 함수 호출 언패킹: 언패킹 연산자(*)를 이용
def add(x, y, z):
    return x + y + z

numbers = [1, 2, 3]
result = add(*numbers)

print(result) # 출력: 6

# 3. zip(*)을 이용한 언패킹
names = ['Ali', 'Bin', 'Coh']
scores = [85, 90, 86]
zipped = zip(names, scores) 
zipped_list = list(zipped)

print(zipped, zipped_list)
# zipped는 주소값: <zip object at 0x000002A2888CD300>
# zipped_list는 배열: [('Ali', 85), ('Bin', 90), ('Coh', 86)]

# 4. 딕셔너리 언패킹: 
def intro(name, age, job):
    print(f"Name: {name}, Age: {age}, Job: {job}")

person = {'name': "Ali", 'age': 25, 'job': 'Programmer'}

intro(**person)  # Name: Ali, Age: 25, Job: Programmer

## ** 연산자를 안 쓴다면 아래처럼 해야 함
# intro(name=person['name'], age=person['age'], job=person['job'])

# 설명
# 1. 인자 전달: intro(name=person['name'], age=person['age'], job=person['job'])
# 2. 함수에 인자 정의: def intro(name='Alice', age=25, job='Engineer')
# 3. 출력 결과: Name: Ali, Age: 25, Job: Programmer

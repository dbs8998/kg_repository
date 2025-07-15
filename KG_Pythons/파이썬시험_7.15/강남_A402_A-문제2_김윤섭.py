import random


random_int = random.randint(1,100)

while True:
    try:
        num = int(input('1~100 사이의 숫자를 입력하세요.'))

        if num > 100 or num <= 0:
            raise ValueError('1~100 사이의 숫자를 입력하세요.')
        elif num > random_int:
            print('너무 높아요.')
        elif num < random_int:
            print('너무 낮아요.')
        else:
            print('정답입니다.')
            break

    except ValueError as e:
        print('잘못 입력하셨습니다.', e)
    except Exception as e:
        print('Exception :', e)
        break
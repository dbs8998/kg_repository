
#부모 클래스 생성
class Robot():
    try:
        def __init__(self, name, battery_level):
            battery_level = int(battery_level)

            if int(battery_level) > 100 or int(battery_level) < 0:
                raise ValueError('배터리 용량은 0부터 100사이의 정수만 입력가능합니다.', battery_level)
            
            self.name = name
            self.battery_level = int(battery_level)

        def charge(self):
            if (self.battery_level + 10) <= 100:
                self.battery_level += 10
                print(f'배터리 용량이 10 증가하였습니다.(현재 잔량 : {self.battery_level})')
            else:
                self.battery_level = 100
                print(f'배터리 용량이 가득 찼습니다.(현재 잔량 : {self.battery_level})')


        def status(self):
            print(f"로봇의 이름은 {self.name}이며, 현재 배터리 잔량은 {self.battery_level} 입니다.")

    except ValueError as e:
        print(e)
    except Exception as e:
        print('[Robot Exception] :', e)

#자식 클래스
class CleaningRobot(Robot):
    try:
        def __init__(self, name, battery_level, cleaning_mode="normal"):
            super().__init__(name, battery_level)
            self.cleaning_mode = cleaning_mode

        def start_cleaning(self):
            if (self.battery_level - 10) >= 0:
                self.battery_level -= 10
                print(f'배터리 용량이 10 감소하였습니다.(현재 잔량 : {self.battery_level})')
            else:
                print(f'배터리 용량이 10 이하 입니다. 사용 할 수 없습니다.(현재 잔량 : {self.battery_level})')


    except ValueError as e:
        print(e)
    except Exception as e:
        print('[CleaningRobot Exception] :', e)




try:
    input = input('로봇의 이름과 초기배터리 잔량을 입력하세요.(ex mylobot, 50):').split(',')


    ro2 = CleaningRobot(input[0], input[1])
    ro2.status()
    ro2.charge()
    ro2.start_cleaning()
    print('mode : ', ro2.cleaning_mode)

except ValueError as e:
    print('잘못 입력하셨습니다.', e)
except Exception as e:
    print('[Exception] :', e)


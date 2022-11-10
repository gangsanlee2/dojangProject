def menu_1():
    class Date:
        @staticmethod
        def is_date_valid(date_string):
            year, month, day = map(int, date_string.split('-'))
            return month <=12 and day <=31

    if Date.is_date_valid('2000-10-31'):
        print('올바른  날짜 형식입니다.')
    else:
        print('잘못된 날짜 형식입니다.')

def menu_2():
    class Time:
        def __init__(self,hour,minute,second):
            self.hour = hour
            self.minute = minute
            self.second = second

        @staticmethod
        def is_time_valid(time_string):
            hour, minute, second = map(int, time_string.split(':'))
            return hour <= 24, minute <=59, second <=60

        @classmethod
        def from_string(cls, time_string):
            pass

    time_string = input()

    if Time.is_time_valid(time_string):
        t = Time.from_string(time_string)
        print(t.hour, t.minute, t.second)
    else:
        print('잘못된 시간 형식입니다.')

if __name__ == "__main__":
    while True:
        print("*" * 20)
        choice = int(input("0.종료\n1.연습문제\n2.심사문제\n번호 입력: "))
        menu = ["0.종료", "1.연습문제", "2.심사문제"]
        print("*" * 20)
        if choice == 0:
            print(menu[0])
            break
        elif choice == 1:
            print(menu[1])
            menu_1()
        elif choice == 2:
            print(menu[2])
            menu_2()
        else:
            print(" wrong menu ")

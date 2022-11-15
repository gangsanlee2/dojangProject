def menu_1():
    x = int(input())
    if 11 <= x <= 20:
        print('11~20')
    elif 21 <= x <= 30:
        print('21~30')
    else:
        print('passt nichts')

def menu_2():
    age = int(input())
    balance = 9000
    if age >=19:
        balance -= 1250
    elif 13 <= age <= 18:
        balance -= 1050
    elif 7 <= age <= 12:
        balance -= 650
    else:
        print('falsch')
    print(balance)
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


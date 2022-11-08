def menu_1():
    x = 5
    if x != 10:
        print('ok')

def menu_2():
    price = int(input())
    name = input()
    if name == 'Cash3000':
        price -= 3000
    elif name == 'Cash5000':
        price -= 5000
    print(price)

if __name__ == "__main__":
    while True:
        choice = int(input("0.종료\n1.연습문제\n2.심사문제\n번호 입력: "))
        menu = ["0.종료", "1.연습문제", "2.심사문제"]
        if choice == 0:
            print(menu[0])
            break
        elif choice == 1:
            print(menu[1])
            menu_1()
            print("*" * 20)
        elif choice == 2:
            print(menu[2])
            menu_2()
            print("*" * 20)
        else:
            print(" wrong menu ")
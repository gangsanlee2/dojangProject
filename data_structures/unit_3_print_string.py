def menu_1():
    print('Hello, world')
    print('Python Programming')

def menu_2():
    print('Hello, world!\n'*2)

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

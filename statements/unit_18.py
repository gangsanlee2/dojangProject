def menu_1():
    i = 0
    while True:
        if i % 10 != 3:
            i += 1
            continue
        if i > 73:
            break
        print(i, end=' ')
        i += 1

def menu_2():
    start, stop = map(int, input().split())

    i = start

    while True:
        if i % 10 == 3 and i < stop:
            i += 1
            continue
        if i < stop:
            break
        print(i, end=' ')
        i += 1


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


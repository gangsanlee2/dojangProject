def menu_1():
    i = 2
    j = 5
    while i <= 32 or j >= 1:
        print(i,j)
        i *= 2
        j -= 1

def menu_2():
    x = int(input())
    while x >= 1350:
        x -= 1350
        print(x)
        if x < 0:
            break

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


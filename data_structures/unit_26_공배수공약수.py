def menu_1():
    a = {i for i in range(1,101) if i % 3 == 0}
    b = {i for i in range(1,101) if i % 5 == 0}
    print(a&b)
def menu_2():
    a, b = map(int, input().split())
    a = {i for i in range(1,a+1) if a % i == 0}
    b = {i for i in range(1,b+1) if b % i == 0}

    divisor = a&b

    result = 0
    if type(divisor) == set:
        result = sum(divisor)

    print(result)

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

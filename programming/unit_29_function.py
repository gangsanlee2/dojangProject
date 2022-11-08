def menu_1():
    x = 10
    y = 3

    def get_quotient_remainder(a, b):
        return a // b, a % b

    quotient, remainder = get_quotient_remainder(x, y)
    print('몫:{0}, 나머지:{1}'.format(quotient, remainder))

def menu_2():
    x, y = map(int, input().split())

    def calc(x,y):
        return x+y, x-y, x*y, x/y

    a, s, m, d = calc(x,y)
    print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))

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
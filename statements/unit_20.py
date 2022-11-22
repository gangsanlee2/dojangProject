def menu_1():
    for i in range(1,101):
        if i % 2 == 0 and i % 11 == 0:
            print('FizzBuzz')
        elif i % 2 == 0:
            print('Fizz')
        elif i % 11 == 0:
            print('Buzz')
        else: print(i)

def menu_2():
    x, y = map(int, input().split())
    for i in range(x,y+1):
        if x >= y :
            print('wrong')
        elif i % 5 == 0 and i % 7 != 0:
            print('Fizz')
        elif i % 7 == 0 and i % 5 != 0:
            print('Buzz')
        elif i % 5 == 0 and i % 7 == 0:
            print('FizzBuzz')
        else:
            print(i)


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


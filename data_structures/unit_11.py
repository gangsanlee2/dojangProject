def menu_1():
    year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    pop = [11, 12, 13, 14, 15, 16, 17, 18]
    print(year[-3:])
    print(pop[-3:])

def menu_2():
    n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
    print(n[1::2])

def menu_3():
    x = input().split()
    a = tuple(x)
    print(a)

def menu_4():
    x = input()
    y = input()
    a = x[1::2]
    b = y[::2]
    print(a+b)

if __name__ == "__main__":
    while True:
        print("*" * 20)
        choice = int(input("0.종료\n1.연습문제\n2.연습문제\n3.심사문제\n4.심사문제\n번호 입력: "))
        menu = ["0.종료", "1.연습문제", "2.연습문제", "3.심사문제", "4.심사문제"]
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
        elif choice == 3:
            print(menu[3])
            menu_3()
        elif choice == 4:
            print(menu[4])
            menu_4()
        else:
            print(" wrong menu ")
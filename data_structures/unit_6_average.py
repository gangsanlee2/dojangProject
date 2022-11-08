def menu_1():
    a, b, c = map(int, input('숫자 -10, 20, 30을 쉼표 없이 한칸 띄우고 입력하시오 : ').split())
    print(a + b + c)

def menu_2():
    a = 50
    b = 100
    c = 'None'
    print(a)
    print(b)
    print(c)

def menu_3():
    kor, eng, math, sci = map(int, input().split())
    print(int((kor + eng + math + sci) / 4))

if __name__ == "__main__":
    while True:
        choice = int(input("0.종료\n1.연습문제\n2.심사문제\n번호 입력: "))
        menu = ["0.종료", "1.연습문제", "2.심사문제1","3.심사문제2"]
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
        elif choice == 3:
            print(menu[3])
            menu_3()
            print("*" * 20)
        else:
            print(" wrong menu ")
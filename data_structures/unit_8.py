def menu_1():
    kor = 92
    eng = 47
    math = 86
    sci = 81
    print(kor >= 50 and eng >= 50 and math >= 50 and sci >= 50)

def menu_2():
    kor, eng, math, sci = input().split()
    print(int(kor) >= 90 and int(eng) > 80 and int(math) > 85 and int(sci) >= 80)

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


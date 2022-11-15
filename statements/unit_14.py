def menu_1():
    written_test = 75
    coding_test = True

    if written_test >= 80 and coding_test == True:
        print('verstanden')
    else:
        print('durchgefallen')

def menu_2():
    kor, eng, math, sci = map(int, input().split())
    avg = (kor + eng + math + sci)/4
    if 0 <= kor <= 100 and 0 <= eng <= 100 and 0 <= math <= 100 and 0 <= sci <= 100 and avg >= 80:
        print('verstanden')
    elif 0 <= kor <= 100 and 0 <= eng <= 100 and 0 <= math <= 100 and 0 <= sci <= 100 and avg < 80:
        print('durchgefallen')
    else:
        print('falsch')

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


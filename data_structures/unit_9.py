def menu_1():
    s = '''가나다라마바사아자차카타파하
abcdefghijklmnopopqrstuvwxyz'''
    print(s)

def menu_2():
    s = '''
'가나다라마바사아자차카타파하'
"abcdefghijklmnopopqrstuvwxyz"
'''
    print(s)
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


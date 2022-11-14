def menu_1():
    with open ('words_1.txt', 'r') as file:
        count = 0
        words = file.readlines()
        for word in words:
            if len(word.strip('\n')) <= 10:
                count += 1
        print(count)

def menu_2():
    with open ('words_2.txt','r') as file:
        for word in file:
            print(word.strip(',','.'))

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
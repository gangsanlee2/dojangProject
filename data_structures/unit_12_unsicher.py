def menu_1():
    camille = {
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6
    }
    print(camille['a'])
    print(camille['f'])

def menu_2():
    a = input().split()
    b = input().split()
    for i,j in enumerate(b):
        b[i] = int(j)
    c = dict(zip(a,b))
    print(c)

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


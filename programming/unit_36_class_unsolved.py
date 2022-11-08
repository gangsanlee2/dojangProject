
def menu_1():
    class AdvancedList(list):
        def replace(self, old, new):
            while old in self:
                self[self.index(old)] = new
    x = AdvancedList([1,2,3,1,2,3,1,2,3])
    x.replace(1,100)
    print(x)

def menu_2():
    class Animal:
        def eat(self):
            print('먹다')
    class Wing:
        def flap(self):
            print('파닥거리다')
        def fly(self):
            print('날다')
    class Bird():
        pass

    b = Bird()
    b.eat()
    b.flap()
    b.fly()
    print(issubclass(Bird, Animal))
    print(issubclass(Bird, Wing))

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

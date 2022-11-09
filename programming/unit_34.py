def menu_1():
    class Knight:
        def __init__(self, health, mana, armor):
            self.health = health
            self.mana = mana
            self.armor = armor

        def slash(self):
            print('베기')
    x = Knight(health=542.4, mana=210.3, armor=38)
    print(x.health, x.mana, x.armor)
    x.slash()

def menu_2():
    class Annie:
        def __init__(self, health, mana, ability_power):
            self.health = health
            self.mana = mana
            self.ability_power = ability_power

        def tibbers(self):
            print('티버: 피해량 {0}'.format(self.ability_power*0.65+400))

    health, mana, ability_power = map(float, input().split())

    x = Annie(health=health, mana=mana, ability_power=ability_power)
    x.tibbers()

if __name__ == "__main__":
    while True:
        print("*" * 20)
        choice = int(input("0.종료\n1.연습문제\n2.심사문제\n번호 입력: "))
        print("*" * 20)
        menu = ["0.종료", "1.연습문제", "2.심사문제"]
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

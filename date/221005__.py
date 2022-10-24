
class Unit:
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상유닛 이동]")
        print(f'{self.name} : {location} 방향으로 이동합니다. 속도 {self.speed}')
class AttackUnit(Unit):
    def __init__(self, name, hp,speed, damage) :
        Unit.__init__(self, name, hp,speed)
        self.damage = damage
        print(f'{self.name} 공격유닛이 생성되었습니다.')
        print(f'체력 {self.hp}, 공격력 {self.damage}, 속도 {self.speed}')
    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적을 공격합니다 [ 공격력 {self.damage} ]')
    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다.')
    def move(self, location):
        super().move(location)
        print("공격 유닛 입니다.")
class Scarecrow:
    def __init__(self, name, hp) :
        self.name = name
        self.hp = hp
        print(f'{self.name} 허수아비가 생성되었습니다.')
        print(f'체력 {self.hp}')
    def damaged(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f'\n{self.name}은 허수아비라서 파괴되지 않습니다.\n')
            self.hp = 1
        print(f'{self.name} : {damage} 데미지를 입었습니다.')
        
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
        
# unit1 = Unit("김준경", 10)

# unit2 = AttackUnit("백진암", 100, 5)


# unit3 = Unit("이희성", 12)
# unit3.clocking = True

# if unit3.clocking == True:
#     print(f'{unit3.name}은 클로킹 상태입니다.')

# a = Scarecrow("이희성", 10)
# while 1:
#     i = int(input("넣을 데미지를 적으세요 : "))
#     a.damaged(i)
#     if i == 0:
#         break
a = AttackUnit("김준경", 100, 10, 5)
a.move("왼쪽")
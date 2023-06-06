class Archer:
    hp = 100
    attack = 10
    protection = 6
    critical_damage = 2
    critical_chance = 20

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.hp == other.hp

    def __lt__(self, other):
        return self.hp < other.hp

    def __gt__(self, other):
        return self.hp > other.hp

    def get_info(self):
        return f'Name: {self.name}, HP: {self.hp}, Attack: {self.attack}'

    def fight(self, other):
        while other.hp > 0 and self.hp >0:
            print(f'Hit {self.name} HP: {self.hp}')
            other.hp -= self.attack
            print(f'Hit {other.name} HP: {other.hp}')
            self.hp -= other.attack
        if self.hp > other.hp:
            return print(f'Win {self.name} HP: {self.hp}')
        else:
            return  print(f'Win {other.name} HP: {other.hp}')


class Swordsman:
    hp = 50
    attack = 5
    protection = 6
    critical_damage = 2
    critical_chance = 20


    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.hp == other.hp

    def __lt__(self, other):
        return self.hp < other.hp

    def __gt__(self, other):
        return self.hp > other.hp

    def get_info(self):
        return f'Name: {self.name}, HP: {self.hp}, Attack: {self.attack}'

    def fight(self, other):
        while other.hp > 0 and self.hp > 0:
            print(f'Hit {self.name} HP: {self.hp}')
            other.hp -= self.attack
            print(f'Hit {other.name} HP: {other.hp}')
            self.hp -= other.attack
        if self.hp > other.hp:
            return print(f'Win {self.name} HP: {self.hp}')
        else:
            return print(f'Win {other.name} HP: {other.hp}')

class Magician:
    hp = 10
    attack = 50
    protection = 6
    critical_damage = 2
    critical_chance = 20

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.hp == other.hp

    def __lt__(self, other):
        return self.hp < other.hp

    def __gt__(self, other):
        return self.hp > other.hp

    def get_info(self):
        return f'Name: {self.name}, HP: {self.hp}, Attack: {self.attack}'

    def fight(self, other):
        while other.hp > 0 and self.hp > 0:
            print(f'Hit {self.name} HP: {self.hp}')
            other.hp -= self.attack
            print(f'Hit {other.name} HP: {other.hp}')
            self.hp -= other.attack
        if self.hp > other.hp:
            return print(f'Win {self.name} HP: {self.hp}')
        else:
            return print(f'Win {other.name} HP: {other.hp}')

unit1 = Archer('Player')
unit2 = Swordsman('player 2')


print(unit2 > unit1)
unit1.fight(unit2)
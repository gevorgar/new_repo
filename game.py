class Warrior:
    hp = 100
    attack = 10

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

class Archer(Warrior):
    attack = 10
    protection = 6
    critical_damage = 2
    critical_chance = 20

    def hit(self, other):
        print(f'Hit {self.name} HP: {self.hp}')
        other.hp -= self.attack


class Swordsman(Warrior):
    attack = 5
    protection = 6
    critical_damage = 2
    critical_chance = 20

    def hit(self, other):
        print(f'Hit {self.name} HP: {self.hp}')
        other.hp -= self.attack


class Magician(Warrior):
    attack = 50
    protection = 6
    critical_damage = 2
    critical_chance = 20

    def hit(self, other):
        print(f'Hit {self.name} HP: {self.hp}')
        other.hp -= self.attack

class Game:

    @classmethod
    def fight(self, unit_1, unit_2):
        if isinstance(unit_1, Warrior) and (unit_2, Warrior):
            while unit_1.hp > 0 and unit_2.hp > 0:
                print(f'Hit {unit_1.name} HP: {unit_2.hp}')
                unit_2.hp -= unit_1.attack
                print(f'Hit {unit_2.name} HP: {unit_2.hp}')
                unit_1.hp -= unit_2.attack

    @classmethod
    def is_fight_end(self, unit_1, unit_2):
        if unit_1.hp > unit_2.hp:
            return print(f'Win {unit_1.name} HP: {unit_1.hp}')
        else:
            return print(f'Win {unit_2.name} HP: {unit_2.hp}')


unit1 = Archer('Player 1')
unit2 = Swordsman('player 2')


print(unit2 > unit1)

new_game = Game()
fight_1 = new_game.fight(unit1, unit2)
result = new_game.is_fight_end(unit1, unit2)


class Warrior:
    hp = 100
    attack = 10

    def __init__(self, name):
        self.name = name
        self.wins = 0

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
    @staticmethod
    def warrior_choice(player_number):
        print(f'Игрок {player_number} - Выбор воина: ')
        user_input = int(input(
            'Введите "1" для выбора "Лучника"\nВведите "2" для выбора "Мечника"\nВведите "3" для выбора "Мага"\n'))
        unit_name = input('Введите имя для вашего воина: ')
        if user_input == 1:
            return Archer(unit_name)
        elif user_input == 2:
            return Swordsman(unit_name)
        elif user_input == 3:
            return Magician(unit_name)
        else:
            print('Ошибка! Неверный ввод! Повторите!')
            # return warrior_choice(player_number)


    @staticmethod
    def fight(unit_1, unit_2):
        print(f'Начало сражения: {unit_1.name} c {unit_2.name}')
        if isinstance(unit_1, Warrior) and (unit_2, Warrior):
            while unit_1.hp > 0 and unit_2.hp > 0:
                print(f'Hit {unit_1.name} HP: {unit_1.hp}')
                unit_2.hp -= unit_1.attack
                print(f'Hit {unit_2.name} HP: {unit_2.hp}')
                unit_1.hp -= unit_2.attack

    @staticmethod
    def is_fight_end(unit_1, unit_2):
        if unit_1.hp > unit_2.hp:
            unit_1.wins += 1
            return print(f'Win {unit_1.name} HP: {unit_1.hp}')
        else:
            unit_2.wins += 1
            return print(f'Win {unit_2.name} HP: {unit_2.hp}')


unit1 = Game.warrior_choice(1)
unit2 = Game.warrior_choice(2)


while True:
    fight_1 = Game.fight(unit1, unit2)
    result = Game.is_fight_end(unit1, unit2)
    print(f'Результат: {unit1.name}:{unit1.wins} - {unit2.name}:{unit2.wins}')
    play_again = input('Играем еще раз? Введите "Да" если хотите сыграть еще: ').lower()
    if play_again != 'да':
        break



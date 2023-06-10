import random

class Warrior:
    hp = 100
    attack = 10
    critical_damage = 0
    critical_chance = 0

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

    def hit(self, other):
        if isinstance(other, Warrior):
            print(f'Hit {self.name} HP: {self.hp}')
            other.hp -= random.randint(self.attack, self.critical_damage)

class Archer(Warrior):
    attack = 10
    protection = 5
    critical_damage = 20
    critical_chance = 30

class Swordsman(Warrior):
    attack = 15
    protection = 7
    critical_damage = 30
    critical_chance = 35

class Magician(Warrior):
    attack = 30
    protection = 10
    critical_damage = 60
    critical_chance = 40


class Game:
    unit1_wins = 0
    unit2_wins = 0

    @staticmethod
    def warrior_choice(player_number):
        while True:
            print(f'Игрок {player_number} - Выбор воина: ')
            user_input = int(input(
                'Введите "1" для выбора "Лучника"\nВведите "2" для выбора "Мечника"\nВведите "3" для выбора "Мага"\n'))
            # unit_name = input('Введите имя для вашего воина: ')
            if user_input == 1:
                return Archer(player_number)
            elif user_input == 2:
                return Swordsman(player_number)
            elif user_input == 3:
                return Magician(player_number)
            else:
                print('Ошибка! Неверный ввод! Повторите!')



    @staticmethod
    def fight(unit_1, unit_2):
        print(f'Начало сражения: {unit_1.name} c {unit_2.name}')
        if not isinstance(unit_1, Warrior) or not (unit_2, Warrior):
            return print('Передан неверный параметр')
        else:
            while unit_1.hp > 0 and unit_2.hp > 0:
                unit_1.hit(unit_2)
                unit_2.hit(unit_1)

    @staticmethod
    def is_fight_end(unit_1, unit_2):
        if unit_1.hp > unit_2.hp:
            Game.unit1_wins += 1
            return print(f'Win {unit_1.name} HP: {unit_1.hp}')
        else:
            Game.unit2_wins += 1
            return print(f'Win {unit_2.name} HP: {unit_2.hp}')



unit1_name = input('Введите имя для первого игрока: ')
unit2_name = input('Введите имя второго игрока: ')

while True:
    unit1 = Game.warrior_choice(unit1_name)
    unit2 = Game.warrior_choice(unit2_name)
    fight_1 = Game.fight(unit1, unit2)
    result = Game.is_fight_end(unit1, unit2)
    print(f'Результат: {unit1_name}:{Game.unit1_wins} - {unit2_name}:{Game.unit2_wins}')
    play_again = input('Играем еще раз? Введите "Да" если хотите сыграть еще: ').lower()
    if play_again != 'да':
        print(f'Игра окончена! Результат {unit1_name}:{Game.unit1_wins} - {unit2_name}:{Game.unit2_wins}')
        break



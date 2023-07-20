import random, collections

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

    def __sub__(self, other):
        if isinstance(other, Warrior):
            if isinstance(self, Archer) and isinstance(other, Swordsman):
                self.attack += round(self.attack * 0.1)
            elif isinstance(self, Swordsman) and isinstance(other, Magician):
                self.attack += round(self.attack * 0.1)
            elif isinstance(self, Magician) and isinstance(other, Archer):
                self.attack += round(self.attack * 0.1)
            print(f'Удар {other.name} HP: {other.hp} по {self.name} HP: {self.hp}')
            self.hp -= random.randint(other.attack, other.critical_damage)
            return self.hp

class Archer(Warrior):
    attack = 10
    protection = 5
    critical_damage = 20
    critical_chance = 30

class Swordsman(Warrior):
    attack = 20
    protection = 7
    critical_damage = 30
    critical_chance = 35

class Magician(Warrior):
    attack = 30
    protection = 10
    critical_damage = 60
    critical_chance = 40


class Game:
    __player_wins = 0
    __unit2_wins = 0

    @staticmethod
    def warrior_choice(player_number):
        while True:
            print(f'Игрок {player_number} - Выбор воина: ')
            user_input = int(input(
                'Введите "1" для выбора "Лучника"\nВведите "2" для выбора "Мечника"\nВведите "3" для выбора "Мага"\n'))
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
                unit_2 - unit_1
                unit_1 - unit_2
        if unit_1.hp > unit_2.hp:
            Game.__player_wins += 1
            return print(f'Win {unit_1.name} HP: {unit_1.hp}\nСчет: {unit_1.name}:{Game.__player_wins} - {unit2.name}:{Game.__unit2_wins} ')
        else:
            Game.__unit2_wins += 1
            return print(f'Win {unit_2.name} HP: {unit_2.hp}\nСчет: {unit_1.name}:{Game.__player_wins} - {unit2.name}:{Game.__unit2_wins}')


first_player_list = collections.deque()
second_player_list =collections.deque()



game1 = Game()
player1_name = input('Введите имя для первого игрока: ')
player2_name = input('Введите имя второго игрока: ')
game_mode = int(input('Выберите режим игры. Введите "1" или "5"'))

if game_mode == 1:
    unit1 = game1.warrior_choice(player1_name)
    unit2 = game1.warrior_choice(player2_name)
    fight_1 = game1.fight(unit1, unit2)
elif game_mode == 5:
    for i in range(5):
        unit1 = game1.warrior_choice(player1_name)
        first_player_list.append(unit1)
    for i in range(5):
        unit2 = game1.warrior_choice(player2_name)
        second_player_list.append(unit2)
else:
    print('Неверный ввод')


for unit in range(5):
    fight = game1.fight(first_player_list.popleft(), second_player_list.popleft())

# while True:
#     unit1 = game1.warrior_choice(player1_name)
#     unit2 = game1.warrior_choice(player2_name)
#     fight_1 = game1.fight(unit1, unit2)
#     play_again = input('Играем еще раз? Введите "Да" если хотите сыграть еще: ').lower()
#     if play_again != 'да':
#         break

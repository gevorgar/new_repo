import random

words = ['apple', 'pineapple', 'avocado', 'banana']

choice = random.choice(words)
field ='*'*len(choice)
count = int(input('Введіть кількість спроб вгадати слово: '))
print(f'Програмою обрано слово: {choice}')
print(f'Слово - {field} Кількість спроб {count}')

for i in range(count):
    user_input = input('Введіть букву, або ціле слово: ')
    temp_field = ""
    if len(user_input) == 1:
        for j in range(len(choice)):
            if user_input == choice[j]:
                temp_field = temp_field + user_input
            else:
                temp_field = temp_field + field[j]
        field = temp_field
        print(field)
    else:
        if user_input == choice:
            print(f'Вітаємо, ви вгадали слово: "{choice}"')
            break
        else:
            print(f'Нажаль, ви не вгадали слово: "{choice}"')
            break


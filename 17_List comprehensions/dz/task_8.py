# Развлечение
#
# N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем
# по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i
# включительно. Определите, какие палки остались стоять на месте.
#
# Напишите программу, которая получает на вход количество палок N и количество бросков K.
# Далее идёт K пар чисел L_i, R_i, при этом 1≤ L_i≤ R_i≤ N.
#
# Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если
# j-я палка осталась стоять, или “.”, если j-я палка была сбита.
#
# Пример:
#
# Кол-во палок: 10
# Кол-во бросков: 3
#
# Бросок 1. Сбиты палки с номера 8
# по номер 10
#
# Бросок 2. Сбиты палки с номера 2
# по номер 5
#
# Бросок 3. Сбиты палки с номера 3
# по номер 6
#
# Результат: I.....I...
import random

n = int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))
list_sticks = ['I' for _ in range(n)]

for i_throw in range(k):
    print(f'\nБросок {i_throw + 1}.', end=' ')
    throw = random.randint(0, n - 1)
    if throw == 0:
        left_range = 0
        right_range = random.randint(throw, (n - 1))
    elif throw == (n - 1):
        right_range = n - 1
        left_range = random.randint(0, throw)
    else:
        left_range = random.randint(0, throw)
        right_range = random.randint(throw, (n - 1))
    i = right_range - left_range
    list_sticks[left_range:right_range] = ['.'] * i
    print(f'Сбиты палки с номера {left_range + 1} по номер {right_range}')

print('\nРезультат:', end=' ')
for i in list_sticks:
    print(i, end='')
# Урок информатики
#
# На одном из уроков информатики учитель объяснял тему «Числа с плавающей точкой», но несколько учеников
# никак не могли понять, почему эта точка «плавает» и как вообще выглядят числа в такой форме. Для
# наглядности учитель написал программу, которая берёт число больше десяти и выводит его в формате
# плавающей точки.
#
# Пользователь вводит положительное число x (x > 10). Напишите функцию, которая выводит его в формате
# плавающей точки, то есть x = a *10 ** b, где 1 ≤ a < 10.
#
# Пример 1:
#
# Введите число: 16
#
# Формат плавающей точки: x = 1.6 * 10 ** 1
#
# Пример 2:
#
# Введите число: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
def float_n(n):
    count = 0
    while n > 10:
        n /= 10
        count += 1

    print(f'мантисса - {n}')
    print(f'степень = {count}')
    print(f'Формат плавающей точки: x = {n} * 10 ** {count}')

n = int(input('Введите число: '))
if n > 10:
    float_n(n)
else:
    print('Введено число меньше 10ти!')
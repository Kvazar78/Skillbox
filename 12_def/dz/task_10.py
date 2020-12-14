# НОД
#
# Напишите функцию, вычисляющую наибольший общий делитель двух чисел
def find_divider(a, b):
    if a == 0 or b == 0:
        print(f'НОД равен {a + b}')
    elif a > b:
        a %= b
        find_divider(a, b)
    elif b > a:
        b %= a
        find_divider(a, b)

a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))

find_divider(a, b)

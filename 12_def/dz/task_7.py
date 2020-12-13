# Вторая цифра
#
# Дано положительное действительное число X. Напишите функцию, которая выводит его вторую
# цифру после десятичной точки.
def secondNum(number):
    second_number = int(number * 100) % 10
    print(f'Вторая цифра числа {number} - {second_number}')


number = float(input('Введи число: '))
secondNum(number)
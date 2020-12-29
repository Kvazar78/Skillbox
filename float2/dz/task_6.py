# Число Эйлера
#
# Напишите программу, которая находит сумму нижеприведённого ряда с точностью до 1e-5.
#
# Пример:
#
# Точность: 1e-20
#
# Результат: 2.7182818284590455
import math

precision = float(input('Точность: '))
count = 0
result = 0
member = 1

while member > precision:
    member = 1 / math.factorial(count)
    result += member
    count += 1

print('Результат:', result)
# Округление в России
#
# По российским правилам числа округляются до ближайшего целого числа, а если
# дробная часть числа равна 0.5, то число округляется вверх.
#
# Дано неотрицательное число x, округлите его по этим правилам. Обратите
# внимание, что функция round не годится для этой задачи! Посмотрите
# шпаргалку под видео.
import math

x = float(input('Введи число: '))

if (x * 10) % 10 >= 5:
    x = math.ceil(x)
else:
    x = math.floor(x)

print(f'Округленное будет: {x}')

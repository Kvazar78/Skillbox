import math

def s_side_full(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * (2 * math.pi * r ** 2)
    return side, full

r = int(input('Введи радиус: '))
h = int(input('Введи высоту: '))

side, full = s_side_full(r, h)

print('Площадь боковой поверхности', round(side, 2))
print('Полная площадь', round(full, 2))

# Вот это объёмы 2
# Андрей продолжает писать курсовую работу по физике и теперь ему нужно находить не только объём планеты,
# но и её площадь. Для этого он использует две такие формулы::
#
# Формула для площади сферы: S = 4 * pi * R**2
# Формула для объёма шара: V = (4/3)*pi * R**3
#
# Так как в самом курсовом проекте эти формулы пригодятся ещё не раз, Андрей решил поступить рационально
# и просто написать функцию для каждой формулы.
#
# Напишите программу, которая на вход получает от пользователя радиус планеты (вещественное число) и
# вызывает функции sphereArea и sphereVolume. Реализуйте эти функции: первая считает и выводит на экран
# площадь сферы, вторая - объём шара.
import math

radius = float(input('Введи радиус планеты: '))


def sphereArea(radius):
    s = 4 * math.pi * radius ** 2
    print(f'Площадь поверхности планеты: {round(s, 2)}')


def sphereVolume(radius):
    v = (4 / 3) * math.pi * radius ** 3
    print(f'Объем планеты: {round(v, 2)}')


sphereArea(radius)
sphereVolume(radius)
# Площади

# Муниципалитет хочет построить необычный парк в одном из районов города. Власти остановились
#  на трёх вариантах: изображение на карте в виде круга, прямоугольника или треугольника. 
#  Однако им также нужно понять какую площадь будет занимать тот или иной вариант при разных
#   значениях.

# Напишите программу, которая в зависимости от выбора пользователя вычисляет площадь круга, 
# прямоугольника или треугольника. Для вычисления площади каждой фигуры должна быть написана 
# отдельная функция.

# Площадь круга:

# S = pi * R ** 2

# Площадь прямоугольника:
# S = a * b

# Площадь треугольника:
# S = 1/2 * a * b * sin(alpha)
import math

def userMenu():
    select = input('Площадь чего посчитать (1 - круга, 2 - прямоугольника, 3 - треугольник): ')
    if select == '1':
        radius = float(input('\nВведите радиус круга: '))
        areaSphere(radius)
    elif select == '2':
        a = float(input('\nВведите длину А прямоугольника: '))
        b = float(input('Введите длину B прямоугольника: '))
        areaRectangle(a, b)
    elif select == '3':
        a = float(input('\nВведите длину стороны А треугольника: '))
        b = float(input('Введите длину стороны B треугольника: '))
        alpha = float(input('Введи величину угла между ними: '))
        areaTriangle(a, b, alpha)
    else:
        print('\nСделан не верный выбор! Повторяем ввод...')
        userMenu()

def areaSphere(radius):
    s = math.pi * radius ** 2
    print(f'\nПлощать круга равна: {s}')

def areaRectangle(a, b):
    s = a * b
    print(f'\nПлощать прямогольника равна: {s}')

def areaTriangle(a, b, alpha):
    alpha = math.radians(alpha)
    s = 0.5 * a * b * math.sin(alpha)
    print(f'\nПлощать треугольника равна: {round(s, 2)}')

userMenu()
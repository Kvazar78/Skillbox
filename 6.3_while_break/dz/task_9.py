# Вася выложил своё новое приложение на платформу для начинающих
# разработчиков, на ней пользователи могут ставить оценку приложению
# от −100 до 100. Ему захотелось сравнить количество положительных и
# отрицательных отзывов, для этого он заранее отфильтровал все отзывы так,
# чтобы в конце были те, которые равны нулю.
#
# Напишите программу, которая находит количество положительных и количество
# отрицательных чисел в последовательности. Последовательность заканчивается
# на числе 0.
#
# Пример:
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2
positive_counter = 0
negative_counter = 0
while True:
    ball = int(input('Введите число: '))
    if ball < 0:
        negative_counter += 1
    elif ball > 0:
        positive_counter += 1
    else:
        break
print(f'Кол-во положительных чисел: {positive_counter}')
print(f'Кол-во отрицательных чисел: {negative_counter}')
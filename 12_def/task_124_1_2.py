def a_not_right():
    print('Число а должно быть меньше b!')

a = int(input('Введите левую границу: '))
b = int(input('Введите правую границу: '))

if a > b:
    a_not_right()
    a = int(input('Введите левую границу: '))
    b = int(input('Введите правую границу: '))

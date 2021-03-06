# Число наоборот 2
#
# Пользователь вводит два числа — N и K. Напишите программу, которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке, затем складывает их, снова
# переворачивает и выводит ответ на экран.
#
# Пример:
#
# Введите первое число: 102
#
# Введите второе число: 123
#
#
# Первое число наоборот: 201
#
# Второе число наоборот: 321
#
# Сумма: 522
#
# Сумма наоборот: 225
def reverse(num):
    string = ''
    for i in range(len(str(num)) - 1, -1, -1):
        string += str(num)[i]
    return int(string)

firstNum = int(input('Введите первое число: '))
secondNum = int(input('Введите второе число: '))

print(f'\nПервое число наоборот: {reverse(firstNum)}')
print(f'\nПервое число наоборот: {reverse(secondNum)}')
print(f'\nСумма чисел: {firstNum + secondNum}')
print(f'\nСумма перевернутых чисел: {reverse(firstNum) + reverse(secondNum)}')


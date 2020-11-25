# Напишите программу, которая запрашивает у пользователя число N и
# выводит таблицу суммы для чисел от 1 до N.
num = int(input('Введи число: '))
for row in range(num + 1):
    for col in range(num + 1):
        print(row + col, end = ' ')
    print()
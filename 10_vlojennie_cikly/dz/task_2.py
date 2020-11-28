# Пользователь вводит число N. Напишите программу, которая выводит
# такую “лесенку” из чисел:
size = int(input('Введите число: '))
for row in range(1, size +1):
    for col in range(row):
        print(row, end=' ')
    print()
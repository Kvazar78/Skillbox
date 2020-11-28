# Пользователь вводит число N. Напишите программу, которая по этому
# числу выводит вот такую лесницу из чисел
num = int(input('Введите число: '))

for number in range(num + 1):
    for i in range(number, num + 1):
        print(i, end=' ')
    print()

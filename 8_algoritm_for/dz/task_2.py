# Напишите программу, которая вычисляет сумму нечётных чисел,
# лежащих в диапазоне от единицы до указанного пользователем числа
# включительно.
num = int(input('Введи число: '))
summ = 0
for i in range(1, num +1, 2):
    summ += i
print(f'Сумма нечетных чисел равна {summ}')
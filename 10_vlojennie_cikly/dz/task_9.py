# Напишите программу, которая запрашивает у пользователя число N и
# находит сумму факториалов 1! + 2! + 3! +... + N!
number = int(input('Введи число: '))
fact = 1
summ = 0

for num in range(1, number +1):
    for factorial in range(1, num +1):
        fact *= factorial
    summ += fact
    fact = 1

print(f'Сумма факториалов равна {summ}')
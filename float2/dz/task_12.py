# Сумма ряда

# Пользователь вводит действительное число х и точность precision. Напишите программу, которая по число х вычисляет сумму ряда в точности до precision.

# Операцией возведения в степень и функцией factorial пользоваться нельзя.


# Пример:

# Введите точность: 0.001
# Введите x: 5
# Сумма ряда =  0.2836250150891709

def degree_factor(n):
    factor = (-1)
    for i in range(n + 1):
        factor *= factor
    return factor

def numerator(x, n):
    n *= 2
    degree = x
    for i in range(n + 1):
        degree *= x
    return x

def denominator(n):
    factorial = 1
    if n == 0:
        return factorial
    else:
        for i in range(2, n + 1):
            factorial *= i
        return factorial
    


x = int(input('Введите x: '))
precision = float(input('Введите точность: '))
precision_round = 0

for i in str(precision):
    precision_round += 1
    if i == '.':
        precision_round = 0

n = 0
summ = 0
num = 1

while x > num:
    # summ = ((-1) ** n) * (x ** (2 * n) / (2 * n)!)
    summ = degree_factor(n) * (numerator(x, n) / )
    n += 1
    num += 1
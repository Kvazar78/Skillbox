# Сумма ряда

# Пользователь вводит действительное число х и точность precision. Напишите программу, которая по число х вычисляет сумму ряда в точности до precision.

# Операцией возведения в степень и функцией factorial пользоваться нельзя.


# Пример:

# Введите точность: 0.001
# Введите x: 5
# Сумма ряда =  0.2836250150891709

def degree_factor(n):
    factor = (-1)
    degree = factor
    if n == 0:
        return (degree * (-1))
    elif n == 1:
        return degree
    else:
        for i in range(2, n + 1):
            degree *= factor
        return degree


def numerator(x, n):
    n *= 2
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        degree = x
        for i in range(2, n + 1):
            degree *= x
        return degree

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

n = 0
member = 1
summ_row = 0

while abs(member) > precision:
    # member = ((-1) ** n) * (x ** (2 * n) / (2 * n)!)
    member = degree_factor(n) * (numerator(x, n) / denominator(2 * n))
    summ_row += member
    n += 1

print(summ_row)
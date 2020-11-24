# Дано число x. Напишите программу для вычисления следующего выражения
# (x-1)(x-3)(x-7)...(x-63)/(x-2)(x-4)(x-8)...(x-64)
x = int(input('Введи число Х: '))
result_a = 1
result_b = 1
a = 0
for n in range(0, 6):
    a += 2 ** n
    print(a)
    result_a *= (x - a)
for n in range(1, 7):
    result_b *= (x - 2 ** n)
print(f'Результат выражения при х={x} будет {result_a / result_b}')


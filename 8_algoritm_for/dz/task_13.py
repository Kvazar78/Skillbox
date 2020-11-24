# Даны целые неотрицательные числа a b c d, при этом 0≤c≤ d.
# Выведите в порядке возрастания все числа от a до b, которые дают
# остаток c при делении на d.
a = int(input('Введи a: '))
b = int(input('Введи b: '))
c = int(input('Введи c: '))
d = int(input('Введи d: '))
for i in range(a, b + 1):
    number = i % d
    if number == c:
        print(i)

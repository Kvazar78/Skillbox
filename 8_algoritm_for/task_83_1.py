# Выведите третью степень каждого нечётного числа в диапазоне от
# единицы до указанного пользователем числа включительно.
# Для этого используйте шаг внутри функции range.
n = int(input('Введи число: '))
for i in range(1, n +1, 2):
    print(f'Третья степень нечетного числа {i} - {i ** 3}')
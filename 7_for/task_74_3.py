# Напишите программу, похожую на разобранный предыдущий пример с
# суммой чисел, но только теперь нужно вычислить сумму всех нечётных
# чисел, лежащих в диапазоне, который укажет пользователь.
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
summ = 0
for i in range(first_num, second_num + 1):
    if i % 2 == 1:
        summ += i
print(f'Сумма нечетных чисел от {first_num} до {second_num} равна {summ}')
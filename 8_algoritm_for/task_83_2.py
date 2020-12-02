# Ваню заставили пойти в театр на балет. Ему стало там настолько
# скучно, что он придумал себе очень странное развлечение: считать
# сумму номеров каждого пятого стула в рядах.
#
# Напишите программу для вычисления суммы каждого пятого числа, лежащего
# в диапазоне от единицы до N. Использовать условный оператор нельзя.
#
# Пример:
# Введите число: 21
# Номер стула: 1
# Номер стула: 6
# Номер стула: 11
# Номер стула: 16
# Номер стула: 21
# Сумма: 55
total_chair = int(input('Введи число: '))
summ = 0
for chair in range(1, total_chair +1, 5):
    print(f'Номер стула: {chair}')
    summ += chair
print(f'Сумма: {summ}')
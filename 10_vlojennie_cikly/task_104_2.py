# Пользователь вводит последовательность из N чисел. Напишите программу,
# которая подсчитывает общее количество цифр больше пяти во всей
# последовательности.
quantity_num = int(input('Сколько будет чисел? '))
count = 0

while 0 > quantity_num > 9:
    quantity_num = int(input('Введи нормальное число от 0 до 9! Повтори ввод: '))

while quantity_num > 0:
    num = input('Вводи число: ')
    for i in num:
        if int(i) > 5:
            count += 1
    quantity_num -= 1

print(f'Количество цифр больше пяти (в последовательности), составило {count}')

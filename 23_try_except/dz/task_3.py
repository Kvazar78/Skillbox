# Счастливое число
#
# Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма этих чисел не станет больше
# либо равна 777. Каждое введённое число при этом дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с
# вероятностью 1 к 13 выбрасывала пользователю случайное исключение и завершалась.
import random

summ = 0

with open('file_summa.txt', 'a') as file_to_write:
    while summ < 777:
        num = int(input('Введи число: '))
        summ += num
        try:
            if random.random() < 1/13:
                raise BaseException
            else:
                file_to_write.write(str(summ)+ '\n')
        except BaseException:
            print('Произошло что-то загадочное...')
            break


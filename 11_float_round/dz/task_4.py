# Кодирование сообщений
#
# В компьютерах символы представляются в виде двоичного кода - это нолики и
# единицы. Память компьютера состоит из бит - это один разряд двоичного кода.
# Сообщение состоит из N символов. При кодировании этого сообщения для каждого
# символа выделяется минимально возможное количество бит. С помощью K бит
# можно закодировать 2**K различных вариантов.
#
# Пример 1: в сообщении 8 символов. Тогда K будет равен трём. (2**3 = 8)
#
# Пример 2: в сообщении 10 символов. Если возьмём K = 3, то 2**3 = 8,
# следовательно все символы мы не закодируем.
# Значит, нужно взять K = 4 (2**4 = 16)
#
# Напишите программу, которая выводит сколько нужно минимально выделить бит
# для кодирования сообщения из N символов. Если количество символов - это не
# степень двойки, то вывести соответствующее сообщение. Для этого можно
# использовать проверку “если двоичный логарифм от K не равен K”.
import math

string = input('Введи сообщение: ')
count_symbol = 0

for i in string:
    count_symbol += 1
k = math.log2(count_symbol)
if k - int(k) != 0:
    print(f'\nВведенное количество символов ({count_symbol}) не является степенью 2!')
    k = math.ceil(k)

print(f'\nНеобходимо выделить {int(k)} бит для кодирования сообщения')
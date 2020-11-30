# Напишите программу, которая получает на вход количество уровней пирамиды
# и выводит их на экран, заполняя нечетными числами вот так:
high = int(input('Введи высоту пирамиды: '))
num = 1

for row in range(high):
    for col in range(high * 2):
        if col == (high * 2 // 2) - row:
            for i in range(row + 1):
                print(num, end='\t')
                print('', end='\t')
                num += 2
        else:
            print(' ', end='\t')
    print()
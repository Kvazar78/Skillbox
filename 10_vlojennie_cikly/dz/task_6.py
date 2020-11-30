# Напишите программу, которая считает количество простых чисел в
# заданной последовательности и выводит ответ на экран.
countNum = int(input('Сколько будет чисел? '))
countProst = 0

while countNum > 0:
    noProst = False
    num = int(input('Вводи число: '))
    if num % 2 == 0 and num != 2:
        noProst = True
    else:
        for i in range(3, num // 2):
            if num % 1 == 0:
                noProst = True
                break
            else:
                noProst = False
    if noProst:
        print('Число не простое')
    else:
        print('Число простое')
        countProst += 1
    countNum -= 1

print(f'\nКоличество простых чисел - {countProst}')
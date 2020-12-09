# Простые числа
#
# Пользователь вводит число N - количество чисел в последовательности. Напишите программу,
# которая проверяет сколько из этих чисел являются простыми. Для проверки простоты числа
# реализуйте функцию isPrime
def isPrime(x):
    if x % 2 == 0 and x != 2:
        noProst = True
    else:
        for i in range(3, x // 2):
            if x % i == 0:
                noProst = True
                break
            else:
                noProst = False
    if noProst:
        print('Число не простое')
    else:
        print('Число простое')


num = int(input('Сколько будет чисел? '))

while num > 0:
    number = int(input('Введи число: '))
    isPrime(number)
    num -= 1

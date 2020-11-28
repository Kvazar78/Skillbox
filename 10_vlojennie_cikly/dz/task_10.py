# Наибольшая сумма цифр
#
# Вводится N чисел. Среди натуральных чисел, которые были введены, найдите
# наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
countNum = int(input('Сколько будет чисел? '))
intermediate = 0

while countNum > 0:
    num = input('Вводи число: ')
    if int(num) > intermediate:
        summ = 0
        intermediate = int(num)
        for i in num:
            summ += int(i)
    countNum -= 1

print(f'Макссимальное число из введенных - {intermediate}, сумма его цифр - {summ}')
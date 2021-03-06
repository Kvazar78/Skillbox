# Недоделка 2
#
# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого
# горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно
# было написать код по следующим условиям: программа получает на вход два числа. В первом числе должно
# быть не меньше трёх цифр, во втором числе — не меньше четырёх, иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами, а затем выводится
# их сумма.
#
# И тут вы натыкаетесь на программу, которая была написана прошлым программистом и которая как раз
# решает такую задачу! Однако старший программист сказал вам немного переписать этот код, чтобы он не
# выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше.
# Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и
# вывод их суммы.
def firstNum(num):
    num = str(num % 10) + str(num // 10 % 10) + str(num // 100)
    return int(num)


def secondNum(num):
    num = str(num % 10) + str(num % 1000 // 10) + str(num // 1000)
    return int(num)


first_n = int(input("Введите первое число: "))
second_n = int(input("\nВведите второе число: "))

if 99 < abs(first_n) <= 999:
    first_n = firstNum(first_n)
    print('\nИзмененное первое число:', first_n)
else:
    print('В первом числе не 3 цифры!')

if 999 < abs(second_n) <= 9999:
    second_n = secondNum(second_n)
    print('Измененное второе число:', second_n)
else:
    print('Во втором числе не 4 цифры!')

print(f'\nСумма чисел: {first_n + second_n}')

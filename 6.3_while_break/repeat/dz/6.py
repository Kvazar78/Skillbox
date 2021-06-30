count_negative = 0
count_positive = 0

while True:
    num = int(input('Введите число: '))
    if num == 0:
        break
    elif num > 0:
        count_positive += 1
    else:
        count_negative += 1


print('Кол-во положительных чисел:', count_positive)
print('Кол-во отрицательных чисел:', count_negative)
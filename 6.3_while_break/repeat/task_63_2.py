num = int(input('Введите число: '))
summ = 0

while num != 0:
    last_num = num % 10
    if last_num == 5:
        print('Обнаружен разрыв')
        break
    summ += last_num
    num //= 10
    
print('Сумма равна ', summ)
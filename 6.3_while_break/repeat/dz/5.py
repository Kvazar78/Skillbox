num = int(input('Введи номер билета: '))
start_num = num // 100000 % 10 + num // 10000 % 10 + num // 1000 % 10
end_num = num % 10 + num % 100 // 10 + num % 1000 // 100

if start_num == end_num:
    print('Билет счастливый!')
else:
    print('Билет не счастливый')
deposit = int(input('Введите сумму вклада: '))
percent = int(input('Введите процент по вкладу: '))
result = int(input('Какой суммы необходимо достичь: '))
count_yars = 1

while deposit < result:
    deposit += int(deposit * percent / 100)
    count_yars += 1

print('Потребовалось', count_yars, 'чтобы сумма достигла/превысила', result)
print('На вкладе накопилась сумма - ', deposit)
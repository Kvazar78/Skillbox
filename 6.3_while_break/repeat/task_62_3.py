accumulation = int(input('Сколько отложить денег? '))

while accumulation < 500000:
    summ = int(input('Сколько отложить денег? '))
    accumulation += summ

print(f'Накоплено более чем достаточно денег - {accumulation} рублей')
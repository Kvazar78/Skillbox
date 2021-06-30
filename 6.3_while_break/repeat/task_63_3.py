summ = int(input('Введите стартовую сумму: '))

while summ < 10000:
    num = int(input('Сколько выпало на кубике? '))
    if num == 3:
        print('Вы проиграли всё!')
        summ = 0
        break
    print('Выиграли 500 рублей!')
    summ += 500

print('Игра закончена.')
print('Итого осталось:', summ, 'рублей')
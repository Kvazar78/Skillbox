# Напишите робота для коллекторов. В самом начале он спрашивает имя
# должника и сумму долга, а затем начинает требовать у него погашения
# до тех пор, пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
#
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
client = input('Введите имя должника: ')
debt = int(input('Введите сумму долга: '))
print(f'{client}, ваша задолженнность составляет {debt} рублей.')
while debt > 0:
#    print(f'{client}, ваша задолженнность составляет {debt} рублей.')
    summ = int(input('Сколько рублей вы внесете сейчас, чтобы ее погасить? '))
    debt -= summ
    if debt <= 0:
        print(f'Отлично, {client}! Вы погасили долг. Спасибо!')
        break
    print(f'Маловато, {client}. Давайте еще раз.')
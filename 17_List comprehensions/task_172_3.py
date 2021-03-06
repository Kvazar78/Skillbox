# Повышение цен
#
# Дан список цен на пять товаров с точностью до копейки. Так как экономика
# даёт о себе знать, мы спрогнозировали, что через год придётся повышать
# цены на X процентов, а ещё через один год — ещё на Y процентов.
#
# Напишите программу, которая получает на вход список цен на товары
# (вещественные числа, список генерируется также с помощью list
# comprehensions) и выводит в одну строку общую сумму стоимости товаров
# за каждый год.
#
# Пример:
#
# Цена на товар: 1.09
# Цена на товар: 23.56
# Цена на товар: 57.84
# Цена на товар: 4.56
# Цена на товар: 6.78
#
# Повышение на первый год: 0
# Повышение на второй год: 10
# Сумма цен за каждый год: 93.83 93.83 103.22
def rise(num, pr):
    return (num * (100 + pr) / 100)


list_prices = []
for _ in range(5):
    list_prices.append(float(input('Цена на товар: ')))

first_up = int(input('Повышение на первый год: '))
second_up = int(input('Повышение на второй год: '))

list_pricesFirst = [rise(x, first_up) for x in list_prices]
list_pricesSecond = [rise(x, second_up) for x in list_pricesFirst]

print('Сумма цен за каждый год:', round(sum(list_prices), 2), round(sum(list_pricesFirst), 2), round(sum(list_pricesSecond), 2))
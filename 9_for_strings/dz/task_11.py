# Напишите программу, которая проверяет, верно ли, что введенное
# слово начинается и заканчивается на одну и ту же букву и затем выводит
# соответствующее сообщение.
#
# Пример:
#
# Введите слово: буль
#
# Первая и последняя буквы разные
#
# Пример 2:
#
# Введите слово: булб
#
# Первая и последняя буквы одинаковые
word = input('Введите слово: ')
firstSymbol = ''
lastSymbol = ''
countSymbol = 0
count2 = 0

for symbol in word:
    countSymbol += 1

for symbol in word:
    count2 += 1
    if count2 == 1:
        firstSymbol = symbol
    elif count2 == countSymbol:
        lastSymbol = symbol

if firstSymbol == lastSymbol:
    print('Первая и последняя буквы одинаковые')
else:
    print('Первая и последняя буквы разные')
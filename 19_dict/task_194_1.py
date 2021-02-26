#  Пунктуация
#
# Напишите программу, которая считает количество знаков пунктуации в символьной строке.
#  К знакам пунктуации относятся символы из набора ".,;:!?". Набор должен храниться
#  в виде множества.
#
# Пример:
#
# Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
#
# Количество знаков пунктуации: 6
znak = {'.', ',', ';', ':', '!', '?'}
text = input('Введите строку: ')
count = 0
for sym in text:
    if sym in znak:
        count += 1

print('\nКоличество знаков пунктуации:', count)

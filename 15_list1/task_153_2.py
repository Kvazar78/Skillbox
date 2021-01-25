# Соседи
#
# Дана строка S и номер позиции символа в строке. Напишите программу, которая выводит соседей этого символа и сообщение
# о количестве таких же символов среди этих соседей: их нет, есть ровно один или есть два таких же.
#
# Пример 1:
#
# Введите строку: abbc
# Номер символа: 3
#
# Символ слева: b
# Символ справа: c
#
# Есть ровно один такой же символ.
#
# Пример 2:
#
# Введите строку: abсd
# Номер символа: 3
#
# Символ слева: b
# Символ справа: d
#
#  Таких же символов нет.
string = input('Введите строку: ')
num_symbol = int(input('Номер символа: '))
find_nei = ''

string_list = list(string)

print(f'\nСимвол слева: {string_list[num_symbol - 2]}')
print(f'Символ справа: {string_list[num_symbol]}')

for sym in range(num_symbol - 2, num_symbol + 1):
    find_nei += string_list[sym]

if find_nei.count(string_list[num_symbol - 1]) == 3:
    print('\nЕсть еще два таких же символа.')
elif find_nei.count(string_list[num_symbol - 1]) == 2:
    print('\nЕсть ровно один такой же символ.')
else:
    print('\nТаких же символов нет.')
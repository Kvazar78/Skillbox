# Цифры в строке
#
# Пользователь вводит строку, которая, возможно, содержит пробелы. Напишите программу
# , которая извлекает из этой строки все символы, являющиеся цифрами и составляет
# из них новую строку.
#
# Пример:
#
# Введите строку: пр6и89вет
#
# Цифры: 689
string = input('Введите строку: ')
new_string = ''

for sym in string:
    if sym.isdigit():
        new_string += sym
print(new_string)
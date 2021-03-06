# Непонятно!
#
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id. Видя,
# как он мучается, вы решили добить помочь ему и объяснить эту тему наглядно.
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных, информацию
# о его изменяемости, а также id этого объекта.
#
# Пример 1:
#
# Введите данные: привет
#
# Тип данных: str (строка)
# Неизменяемый (immutable)
# Id объекта: 1705156583984
#
# Пример 2:
# Введите данные: {‘a’: 10, ‘b’: 20}
#
# Тип данных: dict (словарь)
# Изменяемый (mutable)
# Id объекта: 1705205308536
string = input('Введите данные: ')

print('Тип данных: ', end='')
if string[0] == '{' and string[-1] == '}':
    if ':' in string:
        print('dict (словарь)')
    else:
        print('set (множество)')
    change = 'mutable'
elif string[0] == '[' and string[-1] == ']':
    print('list (список)')
    change = 'mutable'
elif string[0] == '(' and string[-1] == ')':
    print('tuple (кортеж)')
    change = 'immutable'
else:
    print('string (строка)')
    change = 'immutable'

if change == 'immutable':
    print('Неизменяемый (immutable)')
else:
    print('Изменяемый (mutable)')

print('Id объекта:', id(string))
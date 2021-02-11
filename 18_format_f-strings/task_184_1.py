def encryption(abc, sym, step):
    id = abc.index(sym) + step
    if id > len(abc) - 1:
        id -= len(abc)
    symbol = abc[id]
    return symbol


string_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alfabet = list(string_abc)
string = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))

list_newString = [' ' if symbol == ' ' else encryption(alfabet, symbol, step) for symbol in string.lower()]

print(*list_newString, sep='')
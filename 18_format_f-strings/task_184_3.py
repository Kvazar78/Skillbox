# Удаление части
#
# На вход в программу подаётся строка, состоящая из прописных и заглавных букв
# кириллицы. Напишите код, который проверяет, каких букв в строке больше, прописных
# или заглавных. Если заглавных букв больше, то сделать все буквы строки заглавными,
# иначе сделать все прописными.
#
# Подсказка: используйте методы islower() и/или isupper().
#
# Пример:
#
# Введите строку: ПитоН - этО хорошО
#
# Результат: питон - это хорошо
#
# Пример 2:
#
# Введите строку: ПиТоН - ЭтО УДоБнО
#
# Результат: ПИТОН - ЭТО УДОБНО
string = input('Введите строку: ')
low_a = 0
uper_a = 0

for sym in string:
    if sym.islower():
        low_a += 1
    else:
        uper_a += 1

if low_a > uper_a:
    print(string.lower())
else:
    print(string.upper())
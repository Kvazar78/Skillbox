# Самое длинное слово
#
# Дана строка, содержащая пробелы. Найдите в ней самое длинное слово, выведите  это
# слово и его длину. Если таких слов несколько, выведите первое из них.
list_word = input('Введи строку: ').split()
max_sym = 0
max_word = ''

for word in list_word:
    if len(word) > max_sym:
        max_sym = len(word)
        max_word = word

print(f'\nСамое длинное слово в строке - {max_word}, количество символов в нем - {max_sym}')
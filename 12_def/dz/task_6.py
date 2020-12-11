# Текстовый редактор

# Мы продолжаем разрабатывать новый текстовый редактор, и в этот раз нам поручили написать 
# для него код, который считает количество любой буквы и любой цифры в тексте (а не только 
# буквы Ы как раньше). 

# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое
#  в нём количество цифр K и букв N. Функция должна вывести на экран информацию о найденных 
#  буквах и цифрах в определенном формате.

# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л

# Количество цифр 0: 2
# Количество букв л: 1
def count_letters(text):
    num = input('Какую цифру ищем? ')
    sym = input('Какую букву ищем? ')
    count_num = 0
    count_sym = 0
    for symbol in text:
        if symbol == num:
            count_num += 1
        elif symbol == sym:
            count_sym += 1
    print(f'\nКоличество цифр {num}: {count_num}\nКоличество букв {sym}: {count_sym}')

text = input('Введите текст: ')
count_letters(text)
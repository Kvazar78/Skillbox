# Разделители символов
#
# Человек хочет сделать рассылку поздравлений для определённого списка людей. Поздравления для разных людей он
# хочет написать по-разному.
#
# Напишите программу, которая запрашивает у пользователя:
#
# Шаблон поздравления (туда вставляется ФИ и возраст)
# ФИ людей (в одну строку, разделяются запятой)
# Возраст каждого человека (в одну строку через пробел)
#
# В конце  программа выводит поздравления и всех именинников в одну строку вместе с их возрастом.
#
# Пример:
#
# Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: С днём рождения, {name}! С {age}-летием тебя!
#
# Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
#
# Возраст людей через пробел: 20 30 18
#
# С днём рождения, Иван Иванов! С 20-летием тебя!
#
# С днём рождения, Петя Петров! С 30-летием тебя!
#
# С днём рождения, Лена Ленова! С 18-летием тебя!
#
# Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18
while True:
    template = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
    if '{name}' in template and '{age}' in template:
        break
    else:
        print('Шаблон введен не верно! Повторите ввод..')

list_names = input('Список людей через запятую: ').split(', ')
list_ages = input('Возраст людей через пробел: ').split()

for i_man in range(len(list_names)):
    string = template.format(name=list_names[i_man], age=list_ages[i_man])
    print(string)

list_birthday_people = [' '.join([list_names[i_man], list_ages[i_man]]) for i_man in range(len(list_names))]

birthday_people = ' '.join(list_birthday_people)

print('\nИменинники:', birthday_people)
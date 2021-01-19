first_string = input('Первое сообщение: ')
second_string = input('Второе сообщение: ')

if (first_string.count('!') + first_string.count('?')) > (second_string.count('!') + second_string.count('?')):
    print(first_string, second_string)
else:
    print(second_string, first_string)
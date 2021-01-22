def input_list(num, name):
    list_temp = []
    for _ in range(num):
        number = int(input(f'Введи число для {name}: '))
        list_temp.append(number)
    return list_temp


list_first = input_list(3, 'первого списка')
list_second = input_list(7, 'второго списка')

print('Первый список:', list_first)
print('Второй список:', list_second)

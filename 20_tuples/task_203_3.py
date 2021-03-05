# Универсальная программа
#
# Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд. При этом он заранее предупредил,
# что скрипт должен уметь работать с любым итерируемым типом данных.
#
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс чётный.
#
# Пример 1:
#
# Допустим, есть такая строка: 'О Дивный Новый мир!'
#
# Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']
#
# Пример 2:
#
# Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
#
# Результат: [100, 300, 0, 'а']
#
# Примечание: для проверки типа можно использовать функцию
#
# isinstance(<элемент>, <тип данных>), которая возвращает True, если элемент принадлежит к этому типу данных,
# и возвращает False в противном случае.
def result(input_string):
    if isinstance(input_string, str):
        print('Это стока')
        result_list = [i_sym for i_index, i_sym in enumerate(input_string) if i_index % 2 == 0]
    elif isinstance(input_string, list):
        print('Это список')
        result_list = [i_elem for i_index, i_elem in enumerate(input_string) if i_index % 2 == 0]
    elif isinstance(input_string, dict):
        print('Это словарь')
        result_list = [i_keys for i_index, i_keys in enumerate(input_string.keys()) if i_index % 2 == 0]
    elif isinstance(input_string, tuple):
        print('Это кортеж')
        result_list = [i_elem for i_index, i_elem in enumerate(input_string) if i_index % 2 == 0]
    return result_list


string = (1, 2, 3, 4, 5)

print('Результат:', result(string))
# Число наоборот

# Вводится последовательность чисел, которая оканчивается нулём. Реализуйте функцию, 
# которая принимает в качестве аргумента каждое число, переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321

# Введите число: 1000
# Число наоборот: 0001

# Введите число: 0
# Программа завершена!

# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.

# Введите число: 1230
# Число наоборот: 321

# Кстати, нули, которые мы убрали, называются ведущими.
# Вариант с удалением ведущих нулей
def revers(number):
    if number == '0':
        print('Программа завершена!')
    else:
        string = ''
        for sym_id in range(len(number), 0, -1):
            string += number[sym_id - 1]
        string = int(string)
        print(f'Число наоборот: {string}')

number = input('Введите число: ')
revers(number)
#  Функция
#
# Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент (его можно вводить с клавиатуры).
#  Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым его
#  появлением включительно.
#
# Если элемента нет вовсе — вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который
#  начинается с него и идёт до конца исходного.
def gen_tuple(rnd_tuple, random_elem):
    new_tuple = tuple()
    if random_elem in rnd_tuple:
        if rnd_tuple.count(random_elem) > 1:
            start = rnd_tuple[rnd_tuple.index(random_elem):]
            end = rnd_tuple[:rnd_tuple.index(random_elem)+1:-1]
            new_tuple = rnd_tuple[start:end:]
            print('Символ тут не один!')
        else:
            new_tuple = rnd_tuple[rnd_tuple.index(random_elem):]
    return new_tuple


rnd_tuple = (1, 'a', 2, 'b', 3, 'c', 'd', 4, 'a', 't')
random_elem = input('Введите случайный элемент: ')
result_tuple = gen_tuple(rnd_tuple, random_elem)
print(result_tuple)

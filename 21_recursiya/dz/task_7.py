# Продвинутая функция sum
#
# Как мы знаем, в Python есть полезная функция sum, которая умеет находить сумму элементов списков. Но иногда базовых
# возможностей функций не хватает для работы и приходится их усовершенствовать.
#
# Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная функция sum. Вот что она должна
# уметь делать:
#
# Складывать числа из списка списков.
# Складывать из набора параметров.
#
# Примеры вызовов функции:
#
# sum([[1, 2, [3]], [1], 3])
# Ответ: 10
#
# sum(1, 2, 3, 4, 5)
# Ответ: 15
def summ(data, summa):
    for i_item in data:
        if isinstance(i_item, int):
            summa += i_item
        else:
            summa = summ(i_item, summa)

    return summa


input_data = [[1, 2, [3]], [1], 3]
# input_data = (1, 2, 3, 4, 5)
total = 0
# input_data = (1, 2, 3, [4, [5]])
print('Ответ', summ(input_data, total))
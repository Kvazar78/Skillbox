#  Ускоряем работу функции
#
# У нас есть функция, которая делает определённые действия с входными данными:
#
# Берёт факториал от числа.
#
# Результат делит на куб входного числа.
#
# И получившиеся число возводит в 10-ю степень.
#
def calculating_math_func(data, dict_fact={}):
    if data in dict_fact:
        result = dict_fact[data]
        print(data, 'есть в словаре :)')
    else:
        start = 1
        result = 1
        if len(dict_fact) != 0:
            result = max(dict_fact)
            print('используем максимальное значение в словаре', result)
            start = max(dict_fact) + 1
            print('старт расчета факториала продолжаем с', start)
        for index in range(start, data + 1):
            result *= index
            dict_fact[index] = result
    result /= data ** 3
    result = result ** 10
    return result

# Однако каждый раз нам приходится делать сложные вычисления, хотя входные и выходные данные одни и те же. И тут наши
#  знания тонкостей Python должны нам помочь.
#
# Оптимизируйте функцию так, чтобы высчитывать факториал для одного и того же числа только один раз.
#
# Подсказка: вспомните, что происходит с изменяемыми данными, если их выставить по умолчанию в параметрах функции.
# def calculating_math_func(num, dict_fact={}):
#     if num == 1:
#         return 1
#     result = num * calculating_math_func(num - 1)
#     print('Факториал числа:', result)
#     result /= num ** 3
#     print('делим на число в кубе', result)
#     result = result ** 10
#     return result

dict_fact = {}
for _ in range(3):
    num = int(input('Введи число: '))

    print('Ответ:', calculating_math_func(num, dict_fact))
    print(dict_fact)
# Текстовый калькулятор
#
# Иван стоит на пороге величайшего открытия (не будем его расстраивать), которое перевернёт представление о всей математике
# и программировании. Имя этому открытию — текстовый калькулятор. Правда, код для своего открытия ему сложно написать самому,
# и поэтому он попросил вас помочь ему. Так что уже можно бежать в патентное бюро.
#
#
# Есть файл calc.txt, в котором хранятся записи вида
#
# 100 + 34
#
# 23 / 4
#
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделённые пробелами.
#
# Операнды — целые числа. Операции — арифметические (включая деление нацело и нахождение остатка).
#
# Напишите программу, которая вычисляет все эти операции и находит сумму их результатов. Пропишите обработку возможных ошибок.
# Программа не должна завершаться при первой же ошибке, она учитывает все верные строки и выводит найденный ответ.
summ = 0
count_line = 0

with open('calc.txt', 'r') as file_to_read:

    for i_line in file_to_read:
        count_line += 1
        expression_list = i_line.strip().split()
        expression_list = [int(expression_list[i]) if i == 0 or i == 2 else expression_list[i]
                           for i in range(len(expression_list))]
        try:
            if len(expression_list) != 3:
                raise Warning(f'В строке {count_line} слишком много операндов - не осилим! Пропускаем...')
            else:
                if expression_list[1] == '/' and expression_list[2] == 0:
                    raise ZeroDivisionError(f'Делить {expression_list[0]} на ноль неправильно! Пропускаем...')
                elif expression_list[1] == '/':
                    result = expression_list[0] / expression_list[2]
                elif expression_list[1] == '+':
                    result = expression_list[0] + expression_list[2]
                elif expression_list[1] == '-':
                    result = expression_list[0] - expression_list[2]
                elif expression_list[1] == '*':
                    result = expression_list[0] * expression_list[2]
                elif expression_list[1] == '%':
                    result = expression_list[0] % expression_list[2]
                elif expression_list[1] == '//':
                    result = expression_list[0] // expression_list[2]
                else:
                    raise SyntaxError(f'В строке {count_line} используется действие, которое'
                                      f' в этой версии калькулятора не предусмотрено! Пропускаем...')
                summ += result
        except (Warning, ZeroDivisionError, SyntaxError) as error:
            print(error)
print('Сумма результатов всех выражений равна:', summ)
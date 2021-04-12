def line_proc1(string, count_line):
    expression_list = string.strip().split()
    expression_list = [int(expression_list[i]) if i == 0 or i == 2 else expression_list[i]
                       for i in range(len(expression_list))]
    if len(expression_list) != 3:
        raise Warning(f'В строке {count_line} слишком много операндов - не осилим! Пропускаем...')
    elif expression_list[1] == '/' and expression_list[2] == 0:
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
        expression_list = [str(i) for i in expression_list]
        select = input(f'Обнаружена ошибка в строке: {" ".join(expression_list)}! \
                Хотите исправить? (да\нет) ')
        if select == 'да':
            result = line_proc1(input('Введите исправленную строку: '), count_line)
        else:
            raise SyntaxError(f'Т.к. строка {count_line} написана с ошибкой ({i_line}) - пропускаем...')
    return result


summ = 0
count_line = 0

with open('calc.txt', 'r') as file_to_read:

    for i_line in file_to_read:
        count_line += 1
        try:
            summ += line_proc1(i_line, count_line)

        except (Warning, ZeroDivisionError, SyntaxError) as error:
            print(str(error))
print('\nСумма результатов всех выражений равна:', summ)
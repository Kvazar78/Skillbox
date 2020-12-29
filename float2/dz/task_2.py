# Генеалогическое древо
#
# Сэм создаёт генеалогические деревья разных семей. Ему постоянно приходится рассчитывать количество
# места, занимаемое именами родителей на экране.
#
# Пользователь вводит имена и фамилии двух родителей. Создайте функцию get_parent_names_total_length
# для Сэма, которая возвращает количество символов в именах матери и отца суммарно, пробелы между
# именем и фамилией тоже учитываем.
#
# Пример:
#
# ФИ отца: Иван Петров
# ФИ матери: Алена Петрова
#
# Символов в ФИ отца: 11
# Символов в ФИ матери: 13
#
# Сумма символов: 24

def count_symbol(name):
    count = 0
    for i in name:
        count += 1
    return count

father_name = input('ФИ отца: ')
mother_name = input('ФИ матери: ')

countSym_fatherName = count_symbol(father_name)
countSym_motherName = count_symbol(mother_name)

print(f'\nСимволов в ФИ отца: {countSym_fatherName}')
print(f'Символов в ФИ матери: {countSym_motherName}')
print(f'\nСумма символов: {countSym_fatherName + countSym_motherName}')
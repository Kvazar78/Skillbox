# Контроль
#
# В любой компании есть список сотрудников. Руководство одной компании хочет знать, на рабочем месте ли сейчас сотрудник.
# У каждого сотрудника есть пропуск со своим ID-номером (это положительное число), список активных пропусков сотрудников
# известен заранее.
#
# Напишите программу, которая сначала запрашивает у пользователя количество сотрудников в офисе, ID их пропусков,
# а затем запрашивает ID пропуска, который нужно найти в этом списке. Если такой есть, то вывести «Сотрудник на месте»,
# а иначе «Сотрудник не работает!».
#
# Пример:
#
# Кол-во сотрудников в офисе: 4
#
# ID сотрудника: 10
#
# ID сотрудника: 20
#
# ID сотрудника: 30
#
# ID сотрудника: 40
#
# Какой ID ищем? 35
#
# Сотрудник не работает!
employee_ID = []
value_employee = int(input('Кол-во сотрудников в офисе: '))

for _ in range(value_employee):
    id = int(input('\nID сотрудника: '))
    employee_ID.append(id)

search_ID = int(input('\nКакой ID ищем? '))
trueID = False

for id in employee_ID:
    if id == search_ID:
        trueID = True

if trueID:
    print('\nСотрудник на месте')
else:
    print('\nСотрудник не работает!')


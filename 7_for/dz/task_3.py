# Бухгалтер устала постоянно считать вручную среднегодовую зарплату
# сотрудников компании и, чтобы облегчить себе жизнь, обратилась к
# программисту.
#
# Напишите программу, которая принимает от пользователя зарплату
# сотрудника за каждый из 12 месяцев и выводит на экран среднюю зарплату за год.
yars_zp = 0
for month in range(12):
    zp = int(input(f'Введите сумму зарплаты за {month +1} месяц: '))
    yars_zp += zp
print(f'Среднегодовая зарплата составляет {yars_zp / 12} рублей.')
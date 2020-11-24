# Ежемесячная стипендия студента составляет educational_grant руб.
# , а расходы на проживание превышают стипендию и составляют expenses руб.
# в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# Составьте программу расчета суммы денег, которую необходимо получить у
# родителей один раз в начале обучения, чтобы можно было прожить учебный год
# (10 месяцев), используя только эти деньги и стипендию.
educational_grant = int(input('Введи размер стипендии: '))
expenses = int(input('Введи расходы на проживание: '))
total_expenses = expenses
total_grant = educational_grant
for rise_in_prices in range(1, 10):
    expenses *= 1.03
    total_expenses += expenses
    total_grant += educational_grant
print(f'Необходимо запросить еще {total_expenses - total_grant} рублей поддержки')
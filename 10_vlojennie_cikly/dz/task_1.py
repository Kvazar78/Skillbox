# Степан пришёл устраиваться на работу, где ему дали тестовое задание
# : проанализировать такую таблицу, понять как она строится и написать
# программу для вывода её на экран.
#
# Помогите Степану реализовать такую программу. Подсказка: номера столбцов.
# А ещё не забудьте про литерал \t для табуляции.
for row in range(6):
    count = row
    for col in range(6):
        if col == 0:
            print(row, end='\t')
        else:
            print(count, end='\t')
        count += 2
    print()
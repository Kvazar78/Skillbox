go_store_flag = False
print('Начался 8-часовой рабочий день')
count_hours = 1
count_tasks = 0

while count_hours <= 8:
    print(f'{count_hours} час')
    num_task = int(input('Сколько задач решит Максим? '))
    count_tasks += num_task
    sel = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if sel == 1:
        go_store_flag = True
    count_hours += 1

print('Рабочий день закончился. Всего выполнено задач: ', count_tasks)
if go_store_flag:
    print('Нужно зайти в магазин.')
else:
    print('Похода в магазин удалось избежать :)')
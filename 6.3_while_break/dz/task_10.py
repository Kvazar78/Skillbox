# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач, которые нужно
# решить до следующего рабочего часа. И вдобавок каждый час Максиму
# звонит супруга. Он знает, что если он возьмёт трубку, то жена попросит
# зайти вечером в магазин.
#
# Напишите программу, в которой считается, сколько задач выполнил
# Максим за день (8 часов). Если он хоть раз взял трубку, то в конце
# дополнительно выводите сообщение: «Нужно зайти в магазин».
#
# Пример:
# Начался 8-часовой рабочий день
# 1 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? 0
# 2 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? 0
# 3 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? 0
# 4 час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? 1
# 5 час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? 0
# 6 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? 0
# 7 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? 1
# 8 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? 0
# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин
vz_tr_tel = False
hours = 0
tasks = 0
print('Начася 8-часовой рабочий день')
while hours < 8:
    hours += 1
    print(hours, 'час')
    task = int(input('Сколько задач решит Максим? '))
    tasks += task
    wife = int(input('Звонит жена. Взять трубку? 0/1: '))
    if wife:
        vz_tr_tel = True
print(f'Рабочий день закончился. Всего выполнено задач: {tasks}')
if vz_tr_tel == True:
    print('Нужно зайти в магазин')
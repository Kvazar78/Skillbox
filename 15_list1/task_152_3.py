# Собачьи бега
#
# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон. На огромном табло
# выводятся очки каждой собаки. Однако при выводе был обнаружен баг: собаки с наибольшим и наименьшим количеством очков
# поменялись местами! Нужно это исправить.
#
# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.
list_scores = [10, 14, 9, 10, 1]
print(f'Багованный сисок: {list_scores}')
maximum = list_scores[0]
minimum = list_scores[0]

for i in list_scores:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i

for i in range(len(list_scores)):
    if list_scores[i] == minimum:
        list_scores[i] = maximum
    elif list_scores[i] == maximum:
        list_scores[i] = minimum

print(f'Пофиксенный список: {list_scores}')
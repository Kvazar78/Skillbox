quantity_bags = int(input('Сколько всего мешков? '))
count_bags = 0
total_weight = 0

while count_bags < quantity_bags:
    weight = int(input('Сколько весит мешок? '))
    total_weight += weight
    count_bags += 1
    print(f'Уже перенесли {count_bags} мешков из {quantity_bags}')

print('Общий вес мешков составляет: ', total_weight)
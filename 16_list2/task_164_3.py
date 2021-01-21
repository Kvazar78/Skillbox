goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))

goods.append([fruit_name, price])
print('\nНовый ассортимент:', goods)

for i in goods:
    i[1] = round(i[1] * 1.08, 1)

print('\nНовый ассортимент с увел. ценой:', goods)

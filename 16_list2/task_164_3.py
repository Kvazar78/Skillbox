goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))

goods.append([fruit_name, price])
print('Новый ассортимент:', goods)

print(goods[1][1])

# for i in goods:

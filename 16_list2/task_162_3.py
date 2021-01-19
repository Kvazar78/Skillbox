films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',  'Леон', 'Богемская рапсодия', 'Город грехов',  'Мементо', 'Отступники', 'Деревня',  'Проклятый остров', 'Начало', 'Матрица']
list_favorites = []

while True:
    print('\nВаш текущий топ фильмов: ', list_favorites)
    my_film = input('Введи название фильма: ')
    if my_film in list_favorites:
        print('Такой фильм в коллекции уже есть! Выбери другой...')
    else:
        select = input('Выбери действие (добавить, удалить, вставить): ')
        if select == 'добавить':
            list_favorites.append(my_film)
        elif select == 'удалить':
            list_favorites.remove(my_film)
        elif select == 'вставить':
            print(list_favorites)
            place = int(input('Выбери позицию куда добавить фильм: '))
            list_favorites.insert(place - 1, my_film)

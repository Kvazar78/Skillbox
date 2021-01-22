violator_songs = [['World in My Eyes', 4.86],
                  ['Sweetest Perfection', 4.43],
                  ['Personal Jesus', 4.56],
                  ['Halo', 4.9],
                  ['Waiting for the Night', 6.07],
                  ['Enjoy the Silence', 4.20],
                  ['Policy of Truth', 4.76],
                  ['Blue Dress', 4.29],
                  ['Clean', 5.83]]
count_track = int(input('Сколько песен выбрать? '))
timer = 0

for i in range(count_track):
    name_track = input(f'Название {i + 1} песни: ')
    for track in violator_songs:
        if name_track == track[0]:
            timer += track[1]

print(f'\nОбщее время звучания песен: {round(timer, 2)} минут')
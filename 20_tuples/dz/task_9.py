value = int(input('Сколько записей вносится в протокол? '))

competition_book = dict()
winer_list = dict()

for i in range(1, value +1):
    player = tuple(input(f'{i} запись: ').split())
    i_score, i_player = player
    if int(i_score) not in competition_book.keys():
        competition_book[int(i_score)] = [i_player]
    else:
        competition_book[int(i_score)].append(i_player)

count_winners = 0

while count_winners != 3:
    for i_score in sorted(competition_book.keys(), reverse=True):
        for i_player in competition_book[i_score]:
            if i_player not in winer_list.keys():
                winer_list[i_player] = i_score
                count_winners += 1
        if count_winners == 3:
            break

for i_place, i_player, i_score in enumerate(winer_list):
    print(f'{i_place + 1} место. {i_player} ({i_score})')

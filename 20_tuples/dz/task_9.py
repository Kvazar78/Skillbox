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

win_flag = False

for i_score in sorted(competition_book.keys(), reverse=True):
    if win_flag:
        break
    else:
        for i_player in competition_book[i_score]:
            if len(winer_list.keys()) != 3:
                if i_player not in winer_list.keys():
                    winer_list[i_player] = i_score
                # count_winners += 1
            else:
                win_flag = True
                break

count = 1
for i_player, i_score in winer_list.items():
    print(f'{count} место. {i_player} ({i_score})')
    count += 1

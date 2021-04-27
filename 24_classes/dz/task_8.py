from random import randint


class Cards:
    list_color = ['Черви', 'Буби', 'Пики', 'Крести']
    list_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'В', 'Д', 'К', 'Т']

    def __init__(self):
        self.deck = [str(i_card) + ' ' + i_color for i_color in self.list_color for i_card in self.list_cards]

    def hand_over(self):
        return self.deck.pop(randint(0, len(self.deck)))

    def score(self, player_cards):
        score_cards = 0
        for i_card in player_cards:
            i_card = i_card.split()
            if i_card[0].isdigit():
                score_cards += int(i_card[0])
            elif i_card[0] == 'Т':
                if score_cards < 11:
                    score_cards += 11
                else:
                    score_cards += 1
            else:
                score_cards += 10
        return score_cards

    def ostatok_v_kolode(self):
        return self.deck


class Player:

    def __init__(self, name, deck):
        self.name = name
        self.player_cards = [deck.hand_over() for _ in range(2)]

    def player_cards_add(self):
        return self.player_cards.append(deck_for_play.hand_over())

    def score(self):
        return deck_for_play.score(self.player_cards)

    def player_cards_info(self):
        info = ''
        for i_card in self.player_cards:
            info += i_card[0] + i_card[1:] + ' '
        return info


deck_for_play = Cards()
player = Player('Ivan', deck_for_play)
diller = Player('Mudak', deck_for_play)

while player.score() <= 21:
    print(player.player_cards_info(), end='. ')
    print(f'У {player.name} на руках {player.score()} очков')
    select = input('Будем брать еще одну карту? да/нет ')
    if select == 'да':
        player.player_cards_add()
    else:
        break

if player.score() > diller.score() and player.score() <= 21:
    print(f'\n{player.name} выиграл!')
else:
    print(f'\n{player.name} проиграл')
    print(player.player_cards_info(), end='. ')
    print(f'У {player.name} на руках {player.score()} очков')
    print(diller.player_cards_info(), end='. ')
    print(f'У {diller.name} на руках {diller.score()} очков')


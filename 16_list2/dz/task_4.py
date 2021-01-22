guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
action = ''

while True:
    print()
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    action = input('Гость пришёл или ушёл? ')
    if action == 'Пора спать':
        break
    else:
        name = input('Имя гостя: ')
        if action == 'пришёл':
            if len(guests) < 6:
                guests.append(name)
                print(f'Привет, {name}!')
            else:
                print(f'Прости, {name}, но мест нет.')
        elif action == 'ушёл':
            guests.remove(name)
            print(f'Пока, {name}!')

print('\nВечеринка закончилась, все легли спать.')
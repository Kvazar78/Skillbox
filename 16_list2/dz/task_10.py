def print_sequence(seq):
    for i in seq:
        print(i, end=' ')


count_num = int(input('Кол-во чисел: '))
sequence = []
sequence_reverse = []

for _ in range(count_num):
    sequence.append(int(input('Число: ')))

for i in range(len(sequence)- 1, -1, -1):
    sequence_reverse.append(sequence[i])

print('\nПоследовательность:', end=' ')
print_sequence(sequence)
print()

if len(sequence) == 1:
    print('\nОдно число?')
elif sequence == sequence_reverse:
    print('\nСписок уже зеркальный, добавлять ни чего не надо')
else:
    for i in range(len(sequence)- 1, -1, -1):
        if i == 0:
            break
        elif sequence[i] != sequence[i - 1]:
            sequence_reverse.remove(sequence_reverse[0])
            break
        elif sequence[i] == sequence_reverse[0]:
            sequence_reverse.remove(sequence_reverse[0])
            # sequence.remove(sequence[-1])
    print('\nНужно приписать чисел:', len(sequence_reverse))
    print('Сами числа:', end=' ')
    print_sequence(sequence_reverse)

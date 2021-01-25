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

if len(sequence) > 1:
    for i in range(count_num):
        if sequence[i] == sequence_reverse[i]:
            print('Список уже зеркальный')

else:
    print('Тут ни чего делать не надо :)')

print('\nПоследовательность:', end=' ')
print_sequence(sequence)
print('\nНужно приписать чисел:', len(sequence_reverse))
print('Сами числа:', end=' ')
print_sequence(sequence_reverse)
amount_pkt = int(input('Кол-во пакетов: '))
list_in = []
list_out = []
err_count = 0
lost_pkt = 0

for i_pkt in range(amount_pkt):
    print('Пакет номер', i_pkt + 1)
    for i_elm in range(4):
        elem = int(input(f'{i_elm + 1} бит: '))
        list_in.append(elem)
    if list_in.count(-1) <= 1:
        err_count += 1
        list_out.extend(list_in)
    else:
        print('Много ошибок в пакете.')
        lost_pkt += 1
    list_in = []

print('\nПолученное сообщение:', list_out)
print('Кол-во ошибок в сообщении:', err_count)
print('Кол-во потерянных пакетов:', lost_pkt)

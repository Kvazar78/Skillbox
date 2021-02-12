def schet(string):
    a = ''
    b = ''
    znak = ''
    flag_s = False
    for sym in string:
        if sym.isdigit():
            b += sym
        else:
            a = b
            b = ''
            znak += sym
    if znak == '+':
        c = int(a) + int(b)
    elif znak == '-':
        c = int(a) - int(b)
    elif znak == '*':
        c = int(a) * int(b)
    return c

def parentheses(string):
    id_start = string.index('(') + 1
    # id_end = string.index(')')
    vir = string[id_start:]
    return schet(vir)


pr = input('Введи пример: ').split(')')
pr1 = ''

for item in pr:
    for sym in item:
        if sym == '(':
            pr1 += parentheses(item)
        else:
            pr1 += sym
    item = pr1
# for i_item in pr:
#     flag = False
#     vir_a = ''
#     vir_b = ''
#     for sym in i_item:
#         if sym == '(':
#             flag = True
#         if flag:
#             vir_b += sym
#         else:
#             vir_a += sym
#     schet(vir)

    # print(itog)

# for sym in pr:
#     if sym == '(':
#         pr1 += parentheses(pr)
# for
#     if sym.isdigit():
#         pr2 += sym
#     pr1 += sym
#     count += 1




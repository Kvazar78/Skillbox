#  Аннуитетный платёж

# Кредит в сумме S млн руб., выданный на n лет под i% годовых, подлежит погашению равными 
# ежегодными выплатами в конце каждого года, включающими процентные платежи и сумму в 
# погашение основного долга. Проценты начисляются в один раз в год. После выплаты третьего 
# платежа достигнута договорённость между кредитором и заёмщиком о продлении срока погашения 
# ма на n_2 лет и увеличении процентной ставки с момента конверсии до i_2%. 
# Напишите программу, которая выводит план погашения оставшейся части долга.

# Используйте следующие формулы (А — размер аннуитетного платежа, его дробную часть 
# округлите до двух знаков, то есть до копеек): 

# A = K * S

# K = (i *(1 + i) ** n) / ((1 + i) ** n - 1)

# Пример:

# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6

 

# Период: 1
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
 
# Период: 2
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
 
# Период: 3
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
 
# Остаток долга: 17409632.774728
 
#  ==================== 
 
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
 
# Период: 1
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
 
# Период: 2
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
 
# Период: 3
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
 
# Период: 4
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
 
# Остаток долга: 0.017039266414940357
def k(i, n):
    k = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return k

def annuity(s, i, n, a):
    for count in range(1, n + 1):
        print(f'\nПериод: {count}')
        print(f'Остаток долга на начало периода: {s}')
        body_kredit = round(a - s * i, 2)
        print(f'Выплачено процентов: {s * i}')
        print(f'Выплачено тела кредита: {body_kredit}')
        s -= body_kredit
    return s


s = float(input('Введите сумму кредита: '))
n = int(input('На сколько лет выдан? '))
i = float(input('Сколько процентов годовых? '))

a = k(i / 100, n) * s
n_first_period = n - 2
s = annuity(s, i / 100, n_first_period, a)

print(f'\nОстаток долга: {s}')
print('\n ====================')

n2 = int(input('\nНа сколько лет продляется договор? '))
i = int(input('Увеличение ставки до: '))

n += n2 - n_first_period
a = k(i / 100, n) * s
s = annuity(s, i / 100, n, a)

print(f'\nОстаток долга: {round(s, 2)}')
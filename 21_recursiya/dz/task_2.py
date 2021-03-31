#  Свой zip 2
#
# Написав аналог функции zip на собеседовании, вы вспомнили, что этот код можно сделать даже лучше, и резко вырвали
#  листок с кодом из рук работодателя, оставив его в недоумении.
#
# Напишите функцию, которая будет полным аналогом функции zip, и сделайте так, чтобы программа работала с любыми
#  итерируемыми типами данных. Циклами и условными операторами (как и функцией isinstance или type) пользоваться нельзя.
# def zipped2(*args, len_zip):
#     list_index = [i for i in range(len_zip)]
#     zip_list = list(map(args))
#     # zip_list = [(iter1[i], iter2[i])for i in range(len_zip)]
#     return zip_list
#
# a = (1, 2, 3, 4, 5, 6)
# b = 'привет'
# c = {1: 's', 2: 'q', 3: 4}
#
#
# len_zip = min(len(a), len(b), len(c))
# print(len_zip)
# print(zipped2(a, b, c, len_zip=len_zip))
def zip2(*args):
    list_tmp = list(map(list, args))
    len_index = min([len(x) for x in list_tmp])
    list_tmp2 = [(i_iter[i]) for i in range(len_index) for i_iter in list_tmp]

    return list_tmp2


def zip1(*args):
    list_tmp = list(map(list, args))
    len_index = min([len(x) for x in list_tmp])
    # list_zip = [(list_tmp[0][i], list_tmp[1][i], list_tmp[2][i]) for i in range(len_index)]
    list_zip = [(list(map(list, args))[i]) for i in range(len_index)]

    return list_zip


a = (1, 2, 3, 4, 5, 6)
b = 'привет'
c = {1: 's', 2: 'q', 4: 4}

print(zip1(a, b, c))
# list_zip = zip1(a, b, c)
# for i in list_zip:
#     print(i)
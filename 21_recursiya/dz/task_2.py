#  Свой zip 2
#
# Написав аналог функции zip на собеседовании, вы вспомнили, что этот код можно сделать даже лучше, и резко вырвали
#  листок с кодом из рук работодателя, оставив его в недоумении.
#
# Напишите функцию, которая будет полным аналогом функции zip, и сделайте так, чтобы программа работала с любыми
#  итерируемыми типами данных. Циклами и условными операторами (как и функцией isinstance или type) пользоваться нельзя.
def zipped2(iter1, iter2, len_iter):
    if len_iter != -1:
        new_list.append((iter1[len_iter], iter2[len_iter]))
        zipped2(iter1, iter2, len_iter - 1)
    return new_list


iter_obj1 = (1, 2, 3, 4, 5, 6)
iter_obj2 = 'привет'
new_list = []

if len(iter_obj1) > len(iter_obj2):
    len_zip = len(iter_obj2) - 1
else:
    len_zip = len(iter_obj1) - 1

print(zipped2(iter_obj1, iter_obj2, len_zip))


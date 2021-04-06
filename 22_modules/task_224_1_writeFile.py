# Сумма чисел
#
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите программу, которая выводит их сумму в выходной файл answer.txt.
#
# Пример:
#
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10
#
# Содержимое файла answer.txt
# 20
read_file = open('numbers.txt', 'r')
write_file = open('answer.txt', 'w')
summ = 0

for i_line in read_file:
    summ += int(i_line)

read_file.close()
write_file.write(str(summ))
write_file.close()
num_files = open('numbers.txt')
summ = 0

for i_line in num_files:
    summ += int(i_line.strip())

num_files.close()
answer_file = open('answer.txt', 'w')
answer_file.write(str(summ))
answer_file.close()
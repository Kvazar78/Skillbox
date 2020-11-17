# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из
# отрезка [a; b], которые кратны числу 3.
start_segment = int(input('Введите начало отрезка: '))
end_segment = int(input('Введите конец отрезка: '))
average = 0
counter = 0
for dot in range(start_segment, end_segment + 1):
    if dot % 3 == 0:
        average += dot
        counter += 1
print(f'среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3 = {average / counter}')
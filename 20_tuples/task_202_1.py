import random

first_tuple = tuple(random.randint(0, 5) for _ in range(5))
second_tuple = tuple(random.randint(-5, 0) for _ in range(5))
triple_tuple = first_tuple + second_tuple

print(first_tuple)
print(second_tuple)
print(triple_tuple)
print('Количество нулей в 3ем кортеже:', triple_tuple.count(0))

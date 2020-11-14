# Петя писал таймер для телефона, но у него что-то пошло не так.
#
# count = 0
# While count <= 10
#  if count == 0:
#    print('Время вышло!')
#  else:
#    print(count)
#    count -= 1
#
# Скопируйте программу в редактор, исправьте ошибки и убедитесь,
# что на экран выводятся числа с 10 до 0 и сообщение «Время вышло!».

count = 10
while count <= 10:
    if count == 0:
        print(count)
        print('Время вышло!')
        break
    print(count)
    count -= 1
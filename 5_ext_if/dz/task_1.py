# Андрей любит играть в компьютерные игры. И в один прекрасный день
# у него появилась классная идея для сюжета своей игры. Чтобы воплотить
# её в жизнь, он начал изучать программирование и геймдизайн. Начал он с
# главного героя и его системы прокачки.
#
# Напишите программу, которая определяет уровень персонажа в компьютерной игре.
# Пользователь вводит число «очков опыта», а программа вычисляет уровень.
# Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта».
# Начальный уровень равен 1.
#
# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4
#
# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2
level =1
score = int(input('Введите количество опыта: '))
if 1000 <= score < 2500:
  print(f'Ваш уровень: {level + 1}')
elif 2500 <= score < 5000:
  print(f'Ваш уровень: {level + 2}')
elif score >= 5000:
  print(f'Ваш уровень: {level + 3}')
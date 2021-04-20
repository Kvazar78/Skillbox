# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
# У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые:
# «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
#
# Вот таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
#
# Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
# Если результат не определён, то возвращается None.
#
# Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:
#
# class Example_1:
#     def __add__(self, other):
#         return Example_2()
#
# class Example_2:
#     answer = 'сложили два класса и вывели'
#
# a = Example_1()
# b = Example_2()
# c = a + b
# print(c.answer)
#
# Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными элементами.
class Water:
    name = 'Вода'
    answer = 'Дождь и гидросфера'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return


class Air:
    name = 'Воздух'
    answer = 'В основном это сила ветра'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return


class Fire:
    name = 'Огонь'
    answer = 'Огненная стихия'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()


class Earth:
    name = 'Земля'
    answer = 'Почва, грунт...'

    def __add__(self, other):
        if isinstance(other, Storm):
            return Mud()


class Storm:
    name = 'Шторм'
    answer = 'Дождь и сильный ветер'

    def __add__(self, other):
        if isinstance(other, Lightning):
            return Tempest()

class Steam:
    name = 'Пар'
    answer = 'Газообразное состояние воды'


class Mud:
    name = 'Грязь'
    answer = 'Вода с землей... Грязь!'


class Lightning:
    name = 'Молния'
    answer = 'Врятли конечно Воздух + Огонь дадут ее... Но по условию это Молния'


class Dust:
    name = 'Пыль'
    answer = 'Ветер с земли поднимает тучи пыли...'

class Lava:
    name = 'Лава'
    answer = 'Огонь и земля породили лаву'


class Tempest:
    name = 'Буря'
    answer = 'Ну... Буря - это буря, не конец света ;)'
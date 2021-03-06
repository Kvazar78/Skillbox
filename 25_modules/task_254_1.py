# Юниты
#
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие «получить урон»
# (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
#
#     Солдат: получает урон, равный переданному значению.
#     Обычный гражданин: получает урон, равный двукратному переданному значению.
#
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).
class Unit:

    def __init__(self, hp=100):
        self.__hp = hp

    def damage(self, value=0):
        pass

    def set_hp(self):
        return self.__hp

class Soldier(Unit):

    def __init__(self, hp):
        super().__init__(hp)


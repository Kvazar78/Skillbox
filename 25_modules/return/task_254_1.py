# Юниты
#
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
#
#     Солдат: получает урон, равный переданному значению.
#     Обычный гражданин: получает урон, равный двукратному переданному значению.
#
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и наследования,
# конечно же).
class Unit:
    __hp = 100

    def get_damaged(self, damage=0):
        self.set_hp(damage)

    def get_hp(self):
        return self.__hp

    def set_hp(self, damage):
        self.__hp = self.get_hp() - damage


class Soldier(Unit):

    def __init__(self):
        super().__init__()


class Civil(Unit):

    def __init__(self):
        super().__init__()

    def get_damaged(self, damage=0):
        self.set_hp(damage * 2)


hit = 15
sol1 = Soldier()
cit1 = Civil()
print(sol1.get_hp())
print(cit1.get_hp())
sol1.get_damaged(hit)
cit1.get_damaged(hit)
print(sol1.get_hp())
print(cit1.get_hp())
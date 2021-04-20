class Parents:

    def __init__(self, name_p, age_p, kids_list=None):
        self.name_p = name_p
        self.age_p = age_p
        self.kids = kids_list if kids_list else []

    def about_me1(self):
        print(f'Меня зовут {self.name_p}. Мне {self.age_p} лет и у меня', end=' ')
        if len(self.kids) == 0:
            print('нет детей... А теперь уже и поздно..')
        else:
            print('есть дети:')
            for i_kids in self.kids:
                print(f'\t{i_kids.name_c}, ему {i_kids.age_c}, он сейчас {i_kids.calmness_c} и он {i_kids.hungry_c}')

    def give_it_hot_and_strong(self, child):
        child.calmness_c = Children.calmness_dict[1]
        return f'\tТеперь {child.name_c} {child.calmness_c}!'

    def feed(self, child):
        child.hungry_c = Children.hungry_dict[1]
        return f'\tТеперь {child.name_c} хотя бы {child.hungry_c}! Может его отпустит...'


class Children:
    hungry_dict = {0: 'голодный', 1: 'сытый'}
    calmness_dict = {0: 'неадекватный', 1: 'адекватный'}

    def __init__(self, parent, name_c, age_c, calmness=0, hungry=0):
        if parent.age_p >= age_c + 16:
            self.name_c = name_c
            self.age_c = age_c
            self.calmness_c = self.calmness_dict[calmness]
            self.hungry_c = self.hungry_dict[hungry]
            parent.kids += [self]
        else:
            self.age_c = age_c
            print('Внимание! Возраст ребенка не по условию!')


mother = Parents('Ира', 40)
kid = Children(mother, 'Вася', 15)
mother.about_me1()

if mother.age_p >= kid.age_c + 16:
    lay_into = input('Может ему втащить чтобы стал адекватным? да/нет ')
    if lay_into == 'да':
        print(mother.give_it_hot_and_strong(kid))
    else:
        feed = input('Может хотя бы покормить? да/нет ')
        if feed == 'да':
            print(mother.feed(kid))
        else:
            print('Придется его посадить на цепь...')

# Поиск элемента 2
#
# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень,
# до которого будет просматриваться структура. Напишите функцию, которая находит заданный пользователем ключ
# в словаре и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В качестве примера можно
# использовать такой словарь:
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац',
            'footer': {
                'h6': 'как меня замучила рекурсия',
                'div': 'снова какой-то блок, теперь в футере и найти его не получается, т.к. выше видимо уже есть',
            }
        }
    }
}


def find_key(site, key, depth=0, depth_flag=False, step=0):
    if key in site:
        return site[key]

    for sub_key in site.values():
        if step == depth and depth_flag:
            result = None
            break
        if isinstance(sub_key, dict):
            result = find_key(sub_key, key, depth, depth_flag, step + 1)
            if result:
                break
    else:
        result = None
    return result

key = input('Какой ключ ищем? ')
select = input('Будем указывать глубину поиска?(да/нет) ')

if select == 'да':
    depth = int(input('Глубина поиска (0 - начальный уровень): '))
    depth_flag = True
    value = find_key(site, key, depth, depth_flag)
else:
    value = find_key(site, key)

if value:
    print('Значение: ', value)
else:
    print('Такого ключа нет')
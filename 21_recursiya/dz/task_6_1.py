from copy import deepcopy
import pprint


def find_key(site, model):
    for sub_key in site.values():
        if 'title' in sub_key:
            sub_key['title'] = f'Куплю/продам {model} недорого'
        elif 'h2' in sub_key:
            sub_key['h2'] = f'У нас самая низкая цена на {model}'
        if isinstance(sub_key, dict):
            find_key(sub_key, model)
    return site


site_template = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать',
        }
    }
}

value = int(input('Сколько требуется сайтов? '))
site = {}
pp = pprint.PrettyPrinter(width=100, indent=4)

for _ in range(value):
    model = input('Введите модель телефона: ')
    site[model] = deepcopy(site_template)
    site[model] = find_key(site[model], model)
    print(f'Сайт для {model}')
    pp.pprint(site)
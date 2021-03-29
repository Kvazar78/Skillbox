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

for _ in range(value):
    model = input('Введите модель телефона: ')
    site[model] = site_template.copy()
    site[model] = find_key(site[model], model)
    print(f'Сайт для {model}')
    print(site)


# for i_elem in site_template.values():
#     print(f"'{i_elem}': {{")
#     if isinstance(site_template[i_elem], dict):
#         for j_elem in i_elem:
#             print(f"\t{j_elem}")
#

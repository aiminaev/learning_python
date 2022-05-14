def create_menu(file_path):
    menu = open(file_path, encoding='utf-8')
    new_menu = [i.replace('\n', '') for i in menu.readlines()]
    return new_menu


def convert_ingredient(line):
    ingredient_list = line.split(' | ')
    return {
        'ingredient_name': ingredient_list[0],
        'quantity': int(ingredient_list[1]),
        'measure': ingredient_list[2]
    }


def convert_book(new_menu):
    cook_book = {}
    name_recipe = ''
    ingredients = []
    for line in new_menu:
        if line.isnumeric():
            continue
        if '|' in line:
            ingredients.append(convert_ingredient(line))
            continue
        if line == '':
            cook_book[name_recipe] = ingredients
            name_recipe = ''
            ingredients = []
            continue
        name_recipe = line
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    menu = create_menu('book.txt')
    book = convert_book(menu)
    for dish in dishes:
        for ingredient in book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }

    return shop_list

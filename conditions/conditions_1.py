age = int(input("Введите возраст: "))
children = int(input("Введите количество детей: "))
institute = input("Учитесь ли в институте? (Да\Нет): ")
height = int(input("Введите рост: "))
weight = int(input("Введите вес: "))

if age > 27 or children >= 2 or institute.lower() == 'да' or height < 150 or weight < 40:
    print('Не годен')
else:
    print('Годен!')
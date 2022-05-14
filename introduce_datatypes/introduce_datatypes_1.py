boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Кто то может остаться без пары')
else:
    boys.sort()
    girls.sort()
    new_zip = zip(boys, girls)
    new_list = list(new_zip)
    print('Идеальные пары: ')

    for pair in new_list:
        print(pair[0], 'и', pair[1])

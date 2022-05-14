month = int(input('Введите месяц: '))
input_date = int(input('Введите дату: '))

if (month == 1 and 21 <= input_date <= 31) or (month == 2 and 1 <= input_date <= 18):
    print('Водолей')
elif (month == 2 and 19 <= input_date <= 29) or (month == 3 and 1 <= input_date <= 20):
    print('Рыбы')
elif (month == 3 and 21 <= input_date <= 31) or (month == 4 and 1 <= input_date <= 19):
    print('Овен')
elif (month == 4 and 20 <= input_date <= 30) or (month == 5 and 1 <= input_date <= 20):
    print('Телец')
elif (month == 5 and 21 <= input_date <= 30) or (month == 6 and 1 <= input_date <= 21):
    print('Близнецы')
elif (month == 6 and 22 <= input_date <= 30) or (month == 7 and 1 <= input_date <= 22):
    print('Рак')
elif (month == 7 and 23 <= input_date <= 31) or (month == 8 and 1 <= input_date <= 22):
    print('Лев')
elif (month == 8 and 23 <= input_date <= 31) or (month == 9 and 1 <= input_date <= 22):
    print('Дева')
elif (month == 9 and 23 <= input_date <= 30) or (month == 10 and 1 <= input_date <= 23):
    print('Весы')
elif (month == 10 and 24 <= input_date <= 31) or (month == 11 and 1 <= input_date <= 22):
    print('Скорпион')
elif (month == 11 and 23 <= input_date <= 30) or (month == 12 and 1 <= input_date <= 21):
    print('Стрелец')
elif (month == 12 and 22 <= input_date <= 31) or (month == 1 and 1 <= input_date <= 20):
    print('Козерог')
else:
    print('Проверьте введенные данные, знак зодиака не найден')

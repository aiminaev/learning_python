salary = int(input('Введите заработную плату в месяц: '))

salary_year = salary * 12

mortgage_size = int(input('Введите, какой процент(%) уходит на ипотеку: '))
life_money = int(input('Введите, какой процент(%) уходит на жизнь: '))

mortgage_spent = int(salary_year * (mortgage_size / 100))
life_money_spent = int(salary_year * (life_money / 100))

print('\nВывод: ', '\nНа ипотеку было потрачено: ', mortgage_spent, ' рублей')
print(f'Было накоплено: {salary_year - mortgage_spent - life_money_spent}', ' рублей')
info = ['2018-01-01', 'yandex', 'cpc', 100]

value = info[-1]

for n in info[-2::-1]:
    value = {n: value}
print(value)

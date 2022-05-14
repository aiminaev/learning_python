queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

requests = {}

for i in queries:
    k = (len(i.split()))
    if k in requests.keys():
        requests[k] += 1
    else:
        requests[k] = 1

all_request = len(queries)

for key, value in requests.items():
    request_percentage = round(value / all_request * 100, 2)
    print(f'Количество запросов из {key} слов от общего числа {request_percentage} %')
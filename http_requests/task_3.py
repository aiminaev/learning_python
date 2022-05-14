import requests
import datetime
from pprint import pprint


def get_questions():
    today = datetime.date.today()
    delta = datetime.timedelta(days=2)
    past = today - delta
    params = {
        'todate': today,
        'fromdate': past,
        'order': 'desc',
        'sort': 'activity',
        'tagged': 'python',
        'filter': 'default',
        'site': 'stackoverflow'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    url = f'https://api.stackexchange.com/2.3/questions'
    resp = requests.get(url, params=params, headers=headers)

    if resp.status_code == 200:
        questions_list = []
        for current_post in resp.json()['items']:
            questions_list.append(current_post['title'])

        return questions_list
    else:
        print('Нет ответа')


questions = get_questions()
pprint(questions)

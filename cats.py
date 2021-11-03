import time

import requests
import json


def get_cats():
    url = 'https://aws.random.cat/meow'
    # Запрос к сайту
    resp = requests.get(url)
    # Ссылка в консоль
    print(resp.json())
    # Перевод ответ в формат json
    response = resp.json()
    # Ссылка на котика
    cat_url = response['file']
    # Переход по ссылке
    r = requests.get(cat_url)
    # Открыть картинку для записи
    with open('cat.jpg', 'wb') as f:
        # Скачивание картинки
        f.write(r.content)
    # Открыть картинку и передать пользователю
    photo = open('cat.jpg', 'rb')
    return photo

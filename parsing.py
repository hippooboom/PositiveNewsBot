from bs4 import BeautifulSoup
from db import set_info
import requests


def get_news(user_id, category):
    # Запись выбранной категории пользователем
    set_info(user_id, category)
    # Адрес сайта с выбранной категорией
    url = 'https://positivnews.ru/category/' + category
    # Запрос к сайту
    resp = requests.get(url)
    # Пустая строка с новостями
    response_news = ''
    # Создание объекта библиотеки парсинга с текстом сайта
    soup = BeautifulSoup(resp.text, 'html.parser')
    # Поиск всех заголовков 4-го уровня с определенным классом
    news_titles = soup.find_all("h4", class_="entry-title title")
    # Просмотр всех заголовков новостей и их запись в переменную в цикле
    for i in news_titles:
        response_news += i.string + '\n'
    # Возврат переменной в функцию, приходит ответ пользователю
    return response_news

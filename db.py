import sqlite3
import aiogram.utils.markdown as fmt


def get_info(user_id):
    # Открыть соединение с бд
    conn = sqlite3.connect("db_user")
    # Создать курсор
    cursor = conn.cursor()
    # Запрос: выбрать все столбцы из таблицы, где id = переданному в функцию
    cursor.execute("select * from user_info WHERE user_id={0}".format(user_id))
    # Получить одну запись
    info = cursor.fetchone()
    # Формирование ответа
    str_info = 'Колличество выбранных категорий\nБизнес: ' + str(info[1]) + '\nЖивотные: ' + str(info[2]) + \
               '\nИстория: ' + str(info[3]) + '\nКультура: ' + str(info[4]) + '\nНаука: ' + str(info[5]) + \
               '\nНовые технологии: ' + str(info[6]) + '\nПозитивные новости: ' + str(info[7]) + \
               '\nПросто хорошие новости: ' + str(info[8]) + '\nХорошие новорсти в мире: ' + str(info[9])
    return str_info


def set_info(user_id, field):
    # Открыть соединение с бд
    conn = sqlite3.connect("db_user")
    # Создать курсор
    cursor = conn.cursor()
    # Запрос: выбрать все столбцы из таблицы, где id = переданному в функцию
    sql_select_query = """select * from user_info where user_id = ?"""
    # Выполнение запроса
    cursor.execute(sql_select_query, (user_id,))
    # Получение одной записи
    records = cursor.fetchone()
    print(records)

    # В записимости от выбранной категории получаем количество нажатий по кнопкам
    get_count = 0
    if field == 'biznes':
        get_count = records[1]
    elif field == 'zhivotnye':
        get_count = records[2]
    elif field == 'istoriya':
        get_count = records[3]
    elif field == 'kultura':
        get_count = records[4]
    elif field == 'nauka':
        get_count = records[5]
    elif field == 'novye-tehnologii':
        field = 'novye_tehnologii'
        get_count = records[6]
    elif field == 'pozitivnye-istorii':
        field = 'pozitivnye_istorii'
        get_count = records[7]
    elif field == 'prosto-horoshie-novosti':
        field = 'prosto_horoshie_novosti'
        get_count = records[8]
    elif field == 'horoshie-novosti-v-mire':
        field = 'horoshie_novosti_v_mire'
        get_count = records[9]
    # Текст нового запроса на обновление: +1 к выбранной категории
    insert_sql = "UPDATE user_info SET {0}={1} WHERE user_id='{2}'".format(field, get_count + 1, user_id)
    # Выполнение запроса
    cursor.execute(insert_sql)
    # Подтверждение изменения в бд
    conn.commit()
    # Закрыть соединение
    cursor.close()


def set_user(user_id):
    # Открыть соединение с бд
    conn = sqlite3.connect("db_user")
    # Создать курсор который делает запросы
    cursor = conn.cursor()
    # Текст запроса. Вставить в таблицу id пользователя
    insert_sql = "INSERT INTO user_info (user_id) VALUES ({0});".format(user_id)
    # Обработка ошибки
    try:
        # Выполнить запрос выше
        cursor.execute(insert_sql)
    # Если пользователь с таким id уже есть - вывод в консоль
    except Exception:
        print('User already in db')
    # Подтверждение изменения в бд
    conn.commit()

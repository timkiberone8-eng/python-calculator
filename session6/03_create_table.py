# Урок 9, шаг 3 (слайды 8-9): подключиться к новой базе sales_data
# и создать в ней таблицу sales.
#
# Запуск из папки session6:
#     python 03_create_table.py
#
# Чем отличается от слайда:
# - пароль postgres вместо 1111.
# - на слайде 8 вместо dbname написано database. psycopg2 понимает
#   оба слова, это одно и то же.
# - строки print на слайде не видно, а в выводе на слайде 9
#   «Таблица создана» есть. Здесь она дописана.

import psycopg2

# Подключение к базе данных "sales_data"
connection = psycopg2.connect(
    database="sales_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

# Создание таблицы "sales" для хранения информации о продажах.
# IF NOT EXISTS: создать, только если такой таблицы ещё нет. Поэтому
# повторный запуск не падает с ошибкой «отношение "sales" уже существует».
# VARCHAR(100): текст не длиннее 100 символов.
# DECIMAL: точное число с дробью, для денег.
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL,
    sale_date DATE
)
""")

# Здесь autocommit нет, поэтому изменения надо сохранить самому.
# Без commit таблица не появится: при закрытии подключения всё,
# что не сохранено, отменяется.
connection.commit()
print("Таблица создана")

cursor.close()
connection.close()

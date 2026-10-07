# Занятие 5 (04.10), запасной план: база данных без PostgreSQL.
#
# Запуск в терминале VS Code:
#     python planv.py
#
# SQLite встроена в Python: ничего ставить не нужно, пароля нет,
# русские буквы работают. Команды SQL те же, что в SQL Shell.
#
# При каждом запуске база создаётся заново: ученики и самолёты
# возвращаются к началу. Испортил данные — перезапусти программу.

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).with_name("kiber.db")

# SQLite пишет ошибки по-английски. Подсказки к самым частым.
HINTS = {
    "syntax error": "опечатка в команде рядом с этим словом",
    "no such table": "нет такой таблицы, список таблиц: таблицы",
    "no such column": "нет такого столбца, посмотри SELECT * FROM таблица",
    "already exists": "такая таблица уже есть",
    "one statement at a time": "по одной команде за раз",
    "unrecognized token": "непонятный символ",
}


def create_database():
    """Создаёт базу заново: таблицы учеников и самолётов с данными."""
    DB_FILE.unlink(missing_ok=True)
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # INTEGER PRIMARY KEY в SQLite — то же, что SERIAL в PostgreSQL:
    # номер ставится сам.
    cursor.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            birthday DATE,
            gpa NUMERIC(3,2),
            is_active BOOLEAN
        )
    """)
    cursor.executemany(
        "INSERT INTO students (name, age, birthday, gpa, is_active) VALUES (?, ?, ?, ?, ?)",
        [
            ("Аня", 15, "2010-03-15", 4.50, True),
            ("Петя", 16, "2009-11-02", 3.80, True),
            ("Оля", 14, "2011-06-20", 4.90, False),
        ],
    )

    cursor.execute("""
        CREATE TABLE aircrafts (
            aircraft_code TEXT PRIMARY KEY,
            model TEXT,
            range INTEGER
        )
    """)
    cursor.executemany(
        "INSERT INTO aircrafts VALUES (?, ?, ?)",
        [
            ("773", "Boeing 777-300", 11100),
            ("763", "Boeing 767-300", 7900),
            ("SU9", "Sukhoi SuperJet-100", 3000),
            ("320", "Airbus A320-200", 5700),
            ("321", "Airbus A321-200", 5600),
            ("319", "Airbus A319-100", 6700),
            ("733", "Boeing 737-300", 4200),
            ("CN1", "Cessna 208 Caravan", 1200),
            ("CR2", "Bombardier CRJ-200", 2700),
        ],
    )

    connection.commit()
    return connection


def print_table(cursor):
    """Печатает результат SELECT ровной таблицей."""
    headers = [column[0] for column in cursor.description]
    rows = [["NULL" if value is None else str(value) for value in row] for row in cursor.fetchall()]

    widths = [len(header) for header in headers]
    for row in rows:
        for i, value in enumerate(row):
            widths[i] = max(widths[i], len(value))

    print(" | ".join(header.ljust(widths[i]) for i, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[i]) for i, value in enumerate(row)))
    print(f"Строк: {len(rows)}")


def main():
    connection = create_database()
    cursor = connection.cursor()

    print("База готова: таблицы students и aircrafts.")
    print("Пиши SQL-команду и Enter. Список таблиц: таблицы. Выход: выход")

    while True:
        try:
            command = input("\nsql> ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not command:
            continue
        if command.lower() in ("выход", "exit", "\\q"):
            break
        if command.lower() in ("таблицы", "\\dt"):
            command = "SELECT name AS table_name FROM sqlite_master WHERE type = 'table'"

        try:
            cursor.execute(command)
        except sqlite3.Error as error:
            # Ошибка не роняет программу: печатаем и ждём следующую команду.
            hint = next((text for key, text in HINTS.items() if key in str(error)), "")
            print(f"Ошибка: {error}" + (f"  ({hint})" if hint else ""))
            continue

        if cursor.description:
            print_table(cursor)
        else:
            connection.commit()
            if cursor.rowcount >= 0:
                print(f"Готово, строк затронуто: {cursor.rowcount}")
            else:
                print("Готово")

    connection.close()
    print("До свидания!")


if __name__ == "__main__":
    main()

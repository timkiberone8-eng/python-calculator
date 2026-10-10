# Урок 5, практикум. Список дел (To-Do list) из презентации.
#
# Запускать из папки urok5:
#     python todo.py
#
# Та же схема, что в «Моей библиотеке», но данные живут в памяти списком,
# а файл читается один раз на старте и пишется один раз на выходе.
# Это второй из двух способов работы с файлом, и разницу стоит проговорить:
#
#   «Моя библиотека» — писать сразу в файл при каждом действии.
#       + ничего не теряется, даже если программу закрыли крестиком
#       − файл дёргается постоянно, менять записи неудобно
#
#   To-Do list — держать список в памяти, сохранить один раз в конце.
#       + быстро, легко менять и удалять
#       − закрыл окно не через пункт «Выход» — всё пропало
#
# ЛОВУШКА ПРЕЗЕНТАЦИИ: на слайдах open() написан без encoding="utf-8".
# На школьной машине Windows подставит cp1251. Проверено: русский текст
# запишется, но файл перестанет быть UTF-8, и при попытке прочитать его
# как UTF-8 (например, открыть в другой программе) будет
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xce.
# Поэтому encoding="utf-8" стоит везде, где открывается файл.

import csv

FILENAME = "tasks.csv"


def load_tasks(filename):
    """Читает задачи из файла. Нет файла — начинаем с пустого списка."""
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                # row — список из одного элемента, берём нулевой
                tasks.append(row[0])
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создаём новый.")
    return tasks


def save_tasks(filename, tasks):
    """Перезаписывает файл текущим списком задач."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task])


def add_task(tasks, task):
    tasks.append(task)


def show_tasks(tasks):
    if not tasks:
        print("Список дел пуст.")
    else:
        print("Ваши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def main():
    tasks = load_tasks(FILENAME)

    while True:
        print("\n1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Сохранить и выйти")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Введите новую задачу: ")
            add_task(tasks, task)
        elif choice == "3":
            save_tasks(FILENAME, tasks)
            print("Задачи сохранены. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()

# Домашнее задание с последнего слайда:
#   1. Добавить удаление задачи (пункт меню + функция delete_task).
#   2. Отмечать задачу выполненной так, чтобы в основном списке её не было,
#      но в файле она сохранялась. Подсказка: писать в файл вторую колонку
#      "да"/"нет" и не показывать те, где стоит "да".

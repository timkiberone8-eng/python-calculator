# Урок 3, шаг 2. Добавили else и finally.
#
# Полная конструкция читается так:
#   try     — пробуем
#   except  — если сломалось вот так, делаем вот это
#   else    — если НЕ сломалось вообще
#   finally — выполняется всегда, сломалось или нет
#
# Зачем else, если можно дописать в конец try? Затем, что в try должно
# лежать только то, что может сломаться. Чем короче try, тем точнее
# понятно, откуда прилетела ошибка.
#
# finally обычно закрывает то, что было открыто: файл, соединение с базой.
# Закроется даже если программа упала.

from calculator_modules.operations.basic import add, subtract, multiply, divide
from calculator_modules.operations.advanced import power, square_root
from calculator_modules.operations.trigonometry import sin, cos, tan


def main():
    print("Добро пожаловать в калькулятор!")

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input(
            "Введите операцию (сложение, вычитание, умножение, деление, "
            "степень, квадратный корень, синус, косинус, тангенс): "
        ).strip().lower()

        if operation == "сложение":
            result = add(a, b)
        elif operation == "вычитание":
            result = subtract(a, b)
        elif operation == "умножение":
            result = multiply(a, b)
        elif operation == "деление":
            result = a / b
        elif operation == "степень":
            result = power(a, b)
        elif operation == "квадратный корень":
            result = square_root(a)
        elif operation == "синус":
            result = sin(a)
        elif operation == "косинус":
            result = cos(a)
        elif operation == "тангенс":
            result = tan(a)
        else:
            result = "Неизвестная операция"

    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно!")
    except ValueError:
        print("Ошибка: введено не число!")
    else:
        # Сюда попадаем, только если в try ничего не сломалось
        print(f"Результат: {result}")
    finally:
        # А сюда — всегда
        print("Операция завершена.")


if __name__ == "__main__":
    main()

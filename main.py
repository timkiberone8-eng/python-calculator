# Стартовое состояние для того, кто входит в группу на занятии 3.
#
# Это ровно то, с чем группа закончила занятие 2:
#   - калькулятор разнесён по модулям (calculator_modules/)
#   - есть try / except, программа не падает от неверного ввода
#
# И ровно то, чего у группы ещё НЕТ и что делается сегодня вместе:
#   - файла __init__.py, то есть папка с модулями пока не пакет
#   - блока else
#   - своего исключения и его ловли
#
# Твоя задача на сегодня та же, что у всех: добавить это сюда своими руками.

from calculator_modules.arithmetic import add, subtract, multiply, divide
from calculator_modules.advanced import power, square_root


def main():
    print("Добро пожаловать в калькулятор!")

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input(
            "Введите операцию (сложение, вычитание, умножение, деление, "
            "степень, квадратный корень): "
        ).strip().lower()

        if operation == "сложение":
            result = add(a, b)
        elif operation == "вычитание":
            result = subtract(a, b)
        elif operation == "умножение":
            result = multiply(a, b)
        elif operation == "деление":
            result = divide(a, b)
        elif operation == "степень":
            result = power(a, b)
        elif operation == "квадратный корень":
            result = square_root(a)
        else:
            result = "Неизвестная операция"

        print(f"Результат: {result}")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно!")
    except ValueError:
        # float("привет") выбрасывает именно ValueError
        print("Ошибка: введено не число!")


if __name__ == "__main__":
    main()

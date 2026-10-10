# Урок 3, шаг 3 и задача 2. Своё собственное исключение.
#
# Встроенных ошибок Python много, но они про язык: не число, деление на ноль,
# нет файла. Про НАШУ задачу язык ничего не знает. "Корень из отрицательного
# числа" — это правило нашей программы, и объявить его должны мы сами.
#
# Своё исключение — это класс, унаследованный от Exception. Всё, больше
# ничего не нужно: тело можно оставить пустым словом pass.

from calculator_modules.operations.basic import add, subtract, multiply, divide
from calculator_modules.operations.advanced import power
from calculator_modules.operations.trigonometry import sin, cos, tan


class NegativeNumberError(Exception):
    """Исключение вызывается, если число отрицательное"""
    pass


def sqrt_with_check(x):
    """Корень с проверкой. Для отрицательного числа выбрасывает своё исключение."""
    if x < 0:
        # raise = выбросить ошибку. Дальше эта строка не выполнится,
        # управление сразу уйдёт в ближайший подходящий except.
        raise NegativeNumberError("Ошибка: корень из отрицательного числа не определён")
    # ** 0.5 это то же самое, что квадратный корень
    return x ** 0.5


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
            result = sqrt_with_check(a)
        elif operation == "синус":
            result = sin(a)
        elif operation == "косинус":
            result = cos(a)
        elif operation == "тангенс":
            result = tan(a)
        else:
            result = "Неизвестная операция"

    except NegativeNumberError as e:
        # "as e" кладёт саму ошибку в переменную e.
        # print(e) печатает тот текст, который мы передали в raise.
        print(e)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно!")
    except ValueError:
        print("Ошибка: введено не число!")
    else:
        print(f"Результат: {result}")
    finally:
        print("Операция завершена.")


if __name__ == "__main__":
    main()

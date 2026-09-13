# Урок 3, шаг 1. try / except — программа перестаёт падать.
#
# До этого коммита любая из двух вещей роняла программу:
#   - ввели "привет" вместо числа  -> ValueError
#   - поделили на ноль             -> ZeroDivisionError (мы прятали его через if)
#
# try: здесь код, который МОЖЕТ сломаться.
# except: что делать, если сломался именно такой ошибкой.
#
# Ловить ошибку по имени важно. Голый "except:" без имени поймает вообще всё,
# включая твои собственные опечатки, и спрячет их. Так делать не надо.

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
            # Теперь делим честно, без проверки на ноль внутри функции.
            # Ошибку поймает except ниже.
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

        print(f"Результат: {result}")

    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно!")
    except ValueError:
        # float("привет") выбрасывает именно ValueError
        print("Ошибка: введено не число!")


if __name__ == "__main__":
    main()

# Урок 2, задача 1. Добавили третий модуль — тригонометрию.
#
# Обрати внимание, что цепочка elif растёт и растёт. Это нормально сейчас,
# но уже видно, что так дальше нельзя. На следующих уроках это обычно
# заменяют словарём "название операции -> функция".

from calculator_modules.operations.basic import add, subtract, multiply, divide
from calculator_modules.operations.advanced import power, square_root
from calculator_modules.operations.trigonometry import sin, cos, tan


def main():
    print("Добро пожаловать в калькулятор!")
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
        result = divide(a, b)
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


if __name__ == "__main__":
    main()

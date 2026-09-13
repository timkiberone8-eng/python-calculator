# Урок 2, шаг 3. Подключаем второй модуль пакета — степень и корень.

from calculator_modules.operations.basic import add, subtract, multiply, divide
from calculator_modules.operations.advanced import power, square_root


def main():
    print("Добро пожаловать в калькулятор!")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input(
        "Введите операцию (сложение, вычитание, умножение, деление, степень, квадратный корень): "
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
        # Корень берётся только от первого числа, второе не используется.
        # Хороший вопрос группе: как быть, что программа всё равно
        # спросила второе число, хотя оно не нужно?
        result = square_root(a)
    else:
        result = "Неизвестная операция"

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()

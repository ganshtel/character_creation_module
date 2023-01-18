import math

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(Number: float) -> None:
    """Вычисляет квадратный корень."""
    return math.sqrt(Number)


def calc(your_number: float) -> None:
    """Вычисляет вычсления."""
    if your_number <= 0:
        return
    answer = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа '
          f'Это будет: {answer}')


print(message)
calc(25.5)

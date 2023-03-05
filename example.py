"""This script calulate square root of number."""

from math import sqrt

message: str = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа'
)


def calculate_square_root(number: float) -> float:
    """Calculte square root."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Return string of calculation."""
    if your_number < 0:
        return 'Корень из отрицательного числа не считается'
    square_root: float = calculate_square_root(your_number)
    return (
        f'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {square_root}'
    )


print(message)
print(calc(25.5))

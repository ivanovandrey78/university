import math

def area(r):
    """
    Вычисляет площадь круга.

    Параметры:
        r (float): Радиус круга.

    Возвращает:
        float: Площадь круга.

    Пример вызова:
        >>> area(5)
        78.53981633974483
    """
    if not isinstance(r, (int, float)):
        raise TypeError("The radius must be a number (int or float)")

    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r

def perimeter(r):
    """
    Вычисляет длину окружности.

    Параметры:
        r (float): Радиус окружности.

    Возвращает:
        float: Длина окружности.

    Пример вызова:
        >>> perimeter(5)
        31.41592653589793
    """
    if not isinstance(r, (int, float)):
        raise TypeError("The radius must be a number (int or float)")

    if r < 0:
        raise ValueError("Radius cannot be negative")

    return 2 * math.pi * r
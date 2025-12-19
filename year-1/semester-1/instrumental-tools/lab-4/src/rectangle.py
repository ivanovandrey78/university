def area(a, b):
    """
    Вычисляет площадь прямоугольника.

    Параметры:
        a (float): Длина первой стороны.
        b (float): Длина второй стороны.

    Возвращает:
        float: Площадь прямоугольника.

    Пример вызова:
        >>> area(4, 5)
        20
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Sides must be numbers (int or float)")

    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")

    return a * b

def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника.

    Параметры:
        a (float): Длина первой стороны.
        b (float): Длина второй стороны.

    Возвращает:
        float: Периметр прямоугольника.

    Пример вызова:
        >>> perimeter(4, 5)
        18
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Sides must be numbers (int or float)")

    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")

    return 2 * (a + b)
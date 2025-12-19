def area(a, h):
    """
    Вычисляет площадь треугольника.

    Параметры:
        a (float): Длина основания треугольника.
        h (float): Высота треугольника, опущенная к основанию.

    Возвращает:
        float: Площадь треугольника.

    Пример вызова:
        >>> area(6, 4)
        12.0
    """
    if a < 0 or h < 0:
        raise ValueError("Negative values are not allowed for base or height")
    return a * h / 2

def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника.

    Параметры:
        a (float): Длина первой стороны.
        b (float): Длина второй стороны.
        c (float): Длина третьей стороны.

    Возвращает:
        float: Периметр треугольника.

    Пример вызова:
        >>> perimeter(3, 4, 5)
        12
    """
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Negative values are not allowed for sides")
    return a + b + c
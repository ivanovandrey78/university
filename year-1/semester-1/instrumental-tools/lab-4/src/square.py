def area(a):
    """
    Вычисляет площадь квадрата.

    Параметры:
        a (float): Длина стороны квадрата.

    Возвращает:
        float: Площадь квадрата.

    Пример вызова:
        >>> area(5)
        25
    """
    if not isinstance(a, (int, float)):
        raise TypeError("The side must be a number (int or float)")

    if a < 0:
        raise ValueError("Side cannot be negative")
    return a * a

def perimeter(a):
    """
    Вычисляет периметр квадрата.

    Параметры:
        a (float): Длина стороны квадрата.

    Возвращает:
        float: Периметр квадрата.

    Пример вызова:
        >>> perimeter(5)
        20
    """
    if not isinstance(a, (int, float)):
        raise TypeError("The side must be a number (int or float)")

    if a < 0:
        raise ValueError("Side cannot be negative")

    return 4 * a
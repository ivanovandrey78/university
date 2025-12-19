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
    if a < 0:
        raise ValueError("Side cannot be negative")
    return 4 * a
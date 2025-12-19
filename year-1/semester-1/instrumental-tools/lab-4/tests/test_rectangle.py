import unittest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        """Тест площади прямоугольника с нормальными сторонами"""
        self.assertEqual(area(4, 5), 20)

    def test_area_zero_side_a(self):
        """Тест площади прямоугольника с нулевой первой стороной"""
        self.assertEqual(area(0, 5), 0)

    def test_area_zero_side_b(self):
        """Тест площади прямоугольника с нулевой второй стороной"""
        self.assertEqual(area(4, 0), 0)

    def test_area_both_zero(self):
        """Тест площади прямоугольника с нулевыми сторонами"""
        self.assertEqual(area(0, 0), 0)

    def test_area_negative_side_a(self):
        """Тест площади прямоугольника с отрицательной первой стороной"""
        with self.assertRaises(ValueError):
            area(-4, 5)

    def test_area_negative_side_b(self):
        """Тест площади прямоугольника с отрицательной второй стороной"""
        with self.assertRaises(ValueError):
            area(4, -5)

    def test_perimeter_normal(self):
        """Тест периметра прямоугольника с нормальными сторонами"""
        self.assertEqual(perimeter(4, 5), 18)

    def test_perimeter_zero_side_a(self):
        """Тест периметра прямоугольника с нулевой первой стороной"""
        self.assertEqual(perimeter(0, 5), 10)

    def test_perimeter_zero_side_b(self):
        """Тест периметра прямоугольника с нулевой второй стороной"""
        self.assertEqual(perimeter(4, 0), 8)

    def test_perimeter_both_zero(self):
        """Тест периметра прямоугольника с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_square(self):
        """Тест периметра квадрата (частный случай прямоугольника)"""
        self.assertEqual(perimeter(5, 5), 20)

    def test_perimeter_negative_side(self):
        """Тест периметра прямоугольника с отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-4, 5)


if __name__ == '__main__':
    unittest.main()
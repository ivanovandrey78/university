import unittest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        """Тест площади квадрата с нормальной стороной"""
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        """Тест площади квадрата с нулевой стороной"""
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        """Тест площади квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            area(-5)

    def test_area_large(self):
        """Тест площади квадрата с большой стороной"""
        self.assertEqual(area(100), 10000)

    def test_area_decimal(self):
        """Тест площади квадрата с дробной стороной"""
        self.assertEqual(area(2.5), 6.25)

    def test_perimeter_normal(self):
        """Тест периметра квадрата с нормальной стороной"""
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        """Тест периметра квадрата с нулевой стороной"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        """Тест периметра квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_perimeter_large(self):
        """Тест периметра квадрата с большой стороной"""
        self.assertEqual(perimeter(100), 400)

    def test_perimeter_decimal(self):
        """Тест периметра квадрата с дробной стороной"""
        self.assertEqual(perimeter(2.5), 10)


if __name__ == '__main__':
    unittest.main()
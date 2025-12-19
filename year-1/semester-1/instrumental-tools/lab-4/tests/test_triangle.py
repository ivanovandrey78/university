import unittest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        """Тест площади треугольника с нормальными параметрами"""
        self.assertEqual(area(6, 4), 12)

    def test_area_zero_base(self):
        """Тест площади треугольника с нулевым основанием"""
        self.assertEqual(area(0, 4), 0)

    def test_area_zero_height(self):
        """Тест площади треугольника с нулевой высотой"""
        self.assertEqual(area(6, 0), 0)

    def test_area_both_zero(self):
        """Тест площади треугольника с нулевыми основанием и высотой"""
        self.assertEqual(area(0, 0), 0)

    def test_area_negative_base(self):
        """Тест площади треугольника с отрицательным основанием"""
        with self.assertRaises(ValueError):
            area(-6, 4)

    def test_area_negative_height(self):
        """Тест площади треугольника с отрицательной высотой"""
        with self.assertRaises(ValueError):
            area(6, -4)

    def test_area_decimal(self):
        """Тест площади треугольника с дробными параметрами"""
        self.assertEqual(area(5.5, 3.2), 8.8)

    def test_perimeter_normal(self):
        """Тест периметра треугольника с нормальными сторонами"""
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero_side(self):
        """Тест периметра треугольника с нулевой стороной"""
        self.assertEqual(perimeter(0, 4, 5), 9)

    def test_perimeter_all_zero(self):
        """Тест периметра треугольника с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_negative_side(self):
        """Тест периметра треугольника с отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_perimeter_decimal(self):
        """Тест периметра треугольника с дробными сторонами"""
        self.assertEqual(perimeter(2.5, 3.5, 4.5), 10.5)

    def test_perimeter_equilateral(self):
        """Тест периметра равностороннего треугольника"""
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_perimeter_isosceles(self):
        """Тест периметра равнобедренного треугольника"""
        self.assertEqual(perimeter(5, 5, 3), 13)


if __name__ == '__main__':
    unittest.main()
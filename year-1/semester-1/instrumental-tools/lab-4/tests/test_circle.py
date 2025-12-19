import unittest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        """Тест площади круга с нулевым радиусом"""
        self.assertEqual(area(0), 0)

    def test_area_normal_radius(self):
        """Тест площади круга с нормальным радиусом"""
        self.assertAlmostEqual(area(5), 78.53981633974483, places=6)

    def test_area_negative_radius(self):
        """Тест площади круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_zero_radius(self):
        """Тест длины окружности с нулевым радиусом"""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_normal_radius(self):
        """Тест длины окружности с нормальным радиусом"""
        self.assertAlmostEqual(perimeter(5), 31.41592653589793, places=6)

    def test_perimeter_negative_radius(self):
        """Тест длины окружности с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_area_large_radius(self):
        """Тест площади круга с большим радиусом"""
        self.assertAlmostEqual(area(100), 31415.926535897932, places=6)

    def test_perimeter_large_radius(self):
        """Тест длины окружности с большим радиусом"""
        self.assertAlmostEqual(perimeter(100), 628.3185307179587, places=6)


if __name__ == '__main__':
    unittest.main()
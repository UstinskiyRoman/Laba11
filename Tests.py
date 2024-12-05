#Устинский Роман 107в1
import unittest
from Functions import multiplication, division, distance, quadratic_equation, geometric_sum

class TestMathFunctions(unittest.TestCase):
    
    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        with self.assertRaises(ValueError):
            division(10, 0)

    def test_distance(self):
        self.assertAlmostEqual(distance(0, 0, 3, 4), 5)

    def test_quadratic_equation(self):
        self.assertEqual(quadratic_equation(1, -3, 2), (2.0, 1.0))

    def test_geometric_sum(self):
        self.assertEqual(geometric_sum(2, 3, 4), 80)

if __name__ == '__main__':
    unittest.main()

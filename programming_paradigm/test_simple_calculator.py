import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(3, 0), 3)
        self.assertEqual(self.calc.subtract(3, 1), 2)

    def test_multiplication(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.multiply(3, 0), 0)
        self.assertEqual(self.calc.multiply(3, 1), 3)

    def test_division(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.divide(3, 0), None)
        self.assertEqual(self.calc.divide(3, 1), 3)
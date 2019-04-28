import unittest

import calculator


class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(20000000, 20000000), 40000000)
        with self.assertRaises(TypeError): calculator.add(20, "2")

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 10), 0)
        self.assertEqual(calculator.subtract(0.01, 0.11), -0.1)
        with self.assertRaises(TypeError): calculator.subtract(20, "2")

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 10), 100)
        self.assertEqual(calculator.multiply(10, 0), 0)
        self.assertEqual(calculator.multiply(10, "2"), "2222222222")

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 10), 1)
        self.assertEqual(calculator.divide(100000000000, 10), 10000000000)
        self.assertEqual(calculator.divide(1, 10), 0.1)
        with self.assertRaises(TypeError): calculator.divide(20, "2")
        with self.assertRaises(ZeroDivisionError): calculator.divide(20, 0)


if __name__ == '__main__':
    unittest.main()

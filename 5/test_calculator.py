import unittest
import calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calc = calculator.Calculator

    def test_add(self):
        self.assertEqual(self.calc.add(self.calc, 3, 4), 7)
        self.assertEqual(self.calc.add(self.calc,20000000,20000000),40000000)
        with self.assertRaises(TypeError): self.calc.add(self.calc,20,"2")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(self.calc, 10, 10), 0)
        self.assertEqual(self.calc.subtract(self.calc, 0.01, 0.11), -0.1)
        with self.assertRaises(TypeError): self.calc.subtract(self.calc,20,"2")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(self.calc,10,10),100)
        self.assertEqual(self.calc.multiply(self.calc, 10, 0), 0)
        self.assertEqual(self.calc.multiply(self.calc, 10, "2"), "2222222222")

    def test_divide(self):
        self.assertEqual(self.calc.divide(self.calc, 10,10),1)
        self.assertEqual(self.calc.divide(self.calc, 100000000000, 10), 10000000000)
        self.assertEqual(self.calc.divide(self.calc, 1, 10), 0.1)
        with self.assertRaises(TypeError): self.calc.divide(self.calc, 20, "2")
        with self.assertRaises(ZeroDivisionError): self.calc.divide(self.calc, 20, 0)


if __name__ == '__main__':
    unittest.main()

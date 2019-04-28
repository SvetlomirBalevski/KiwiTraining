import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 10
        self.y = 5
        self.zero=0

    def test_add(self):
        self.assertEquals(calculator.add(self.x,self.y),15)

    def test_subtract(self):
        self.assertEquals(calculator.subtract(self.x,self.y),5)

    def test_multiply(self):
        self.assertEquals(calculator.multiply(self.x,self.y),50)
        self.assertEquals(calculator.multiply(self.x,self.zero),0)

    def test_divide(self):
        self.assertEquals(calculator.divide(self.x,self.y),2)
        # self.assertRaises(ZeroDivisionError,calculator.divide(self.x,self.zero))

if __name__ == '__main__':
    unittest.main()
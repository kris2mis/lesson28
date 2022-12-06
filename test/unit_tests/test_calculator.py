import unittest

from model.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    # AAA
    def test_sum(self):
        # arrange
        self.calc.a = 10
        self.calc.b = 20
        expected = 30

        # action
        actual = self.calc.sum()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

    def test_sub(self):
        self.calc.a = 10
        self.calc.b = 7
        expected = 3

        actual = self.calc.sub()

        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

    def test_mul(self):
        # arrange
        self.calc.a = 8
        self.calc.b = 7
        expected = 56

        # action
        actual = self.calc.mul()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

    def test_div(self):
        # arrange
        self.calc.a = 18
        self.calc.b = 7
        expected = 2

        # action
        actual = self.calc.div()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)


if __name__ == "__main__":
    unittest.main()

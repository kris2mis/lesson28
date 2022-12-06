import unittest

from model.calculator import Calculator


class TestCalculator(unittest.TestCase):
    calc = Calculator()

    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()
        # TestCalculator.calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        del cls.calc

    # AAA
    def test_sum(self):
        # arrange
        TestCalculator.calc.a = 10
        TestCalculator.calc.b = 20
        expected = 30

        # action
        actual = TestCalculator.calc.sum()

        # assert
        self.assertEqual(expected, actual)

    def test_sub(self):
        TestCalculator.calc.a = 10
        TestCalculator.calc.b = 7
        expected = 3

        actual = TestCalculator.calc.sub()

        self.assertEqual(expected, actual)

    def test_mul(self):
        # arrange
        TestCalculator.calc.a = 8
        TestCalculator.calc.b = 7
        expected = 56

        # action
        actual = TestCalculator.calc.mul()

        # assert
        self.assertEqual(expected, actual)

    def test_div(self):
        # arrange
        TestCalculator.calc.a = 18
        TestCalculator.calc.b = 7
        expected = 2

        # action
        actual = TestCalculator.calc.div()

        # assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

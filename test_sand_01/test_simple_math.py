import unittest

import simple_math


class TestSimpleMath(unittest.TestCase):
    """
    TEST THE FUNCTIONS FROM THE SIMPLE_MATH FILE
    """

    def test_add(self):
        """
        TEST THE ADD FUNCTION
        """
        self.assertEqual(simple_math.add(1, 2), 3)
        self.assertEqual(simple_math.add(0, 0), 0)
        self.assertEqual(simple_math.add(-1, 1), 0)

    def test_subtract(self):
        """
        TEST THE SUBTRACT FUNCTION
        """
        self.assertEqual(simple_math.subtract(1, 2), -1)
        self.assertEqual(simple_math.subtract(0, 0), 0)
        self.assertEqual(simple_math.subtract(-1, 1), -2)

    def test_multiply(self):
        """
        TEST THE MULTIPLY FUNCTION
        """
        self.assertEqual(simple_math.multiply(1, 2), 2)
        self.assertEqual(simple_math.multiply(0, 0), 0)
        self.assertEqual(simple_math.multiply(-1, 1), -1)

    def test_divide(self):
        """
        TEST THE DIVIDE FUNCTION
        """
        self.assertEqual(simple_math.divide(1, 2), 0.5)
        self.assertEqual(simple_math.divide(0, 1), 0)
        self.assertEqual(simple_math.divide(-1, 1), -1)


if __name__ == "__main__":
    unittest.main()

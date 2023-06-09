import unittest

def square(num):
    return num ** 2

class SquareTestCase(unittest.TestCase):
    def test_square_positive_number(self):
        result = square(5)
        self.assertEqual(result, 25)

    def test_square_negative_number(self):
        result = square(-4)
        self.assertEqual(result, 16)

    def test_square_zero(self):
        result = square(0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

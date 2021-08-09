import unittest

from basic_cv.basic_cv.helpers.range import Range
from basic_cv.basic_cv.helpers.limiters import limit_i, limit_l


class LimitersTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.integers = [4, 5, 8, 11, 12]
        self.range = Range(5, 11)
        self.integers_in_range = [5, 5, 8, 11, 11]

    def test_limit_i(self):
        for key, value in enumerate(self.integers):
            self.assertEqual(limit_i(value, self.range), self.integers_in_range[key])

    def test_limit_l(self):
        self.assertEqual(limit_l(self.integers, self.range), self.integers_in_range)


if __name__ == '__main__':
    unittest.main()

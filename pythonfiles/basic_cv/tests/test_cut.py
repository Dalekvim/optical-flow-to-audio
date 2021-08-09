import unittest

import numpy as np

from basic_cv.basic_cv.helpers.cut import cut
from basic_cv.basic_cv.helpers.range import Range


class CutTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = np.arange(9).reshape((3, 3))
        self.matrix_11 = np.array([[4, 5], [7, 8]])
        self.matrix_33 = np.array([[0, 1], [3, 4]])

    def test_cut_normal(self):
        self.assertTrue(np.array_equal(cut(self.matrix, Range(1, 2), Range(1, 2)), self.matrix_11))
        self.assertTrue(np.array_equal(cut(self.matrix, Range(0, 1), Range(0, 1)), self.matrix_33))

    def test_cut_extreme(self):
        self.assertTrue(np.array_equal(cut(self.matrix, Range(1, 2), Range(1, 2)), self.matrix_11))
        self.assertTrue(np.array_equal(cut(self.matrix, Range(0, 1), Range(0, 1)), self.matrix_33))


if __name__ == '__main__':
    unittest.main()

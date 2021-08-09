import unittest

import numpy as np

from basic_cv.basic_cv.helpers.extend import extend


class ExtendTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = np.arange(9).reshape((3, 3))

    def test_normal(self):
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                self.assertEqual(extend(self.matrix, (i, j)), self.matrix.item((i, j)))

    def test_extend(self):
        self.assertEqual(extend(self.matrix, (0, -1)), 0)
        self.assertEqual(extend(self.matrix, (-1, 0)), 0)
        self.assertEqual(extend(self.matrix, (0, 3)), 2)
        self.assertEqual(extend(self.matrix, (3, 0)), 6)
        self.assertEqual(extend(self.matrix, (3, 3)), 8)


if __name__ == '__main__':
    unittest.main()

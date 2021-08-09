import unittest

import numpy as np

from basic_cv.basic_cv.helpers.range import Range


class RangeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.range = Range(5, 11)

    def test_limit(self):
        # Strings cannot be input as the limits of Range.
        self.assertRaises(TypeError, Range, "1", "2")
        self.assertRaises(TypeError, Range, "a", 2)
        self.assertRaises(TypeError, Range, 1, "b")
        self.assertRaises(TypeError, Range, "a", "b")

    def test_values(self):
        # The maximum value of Range cannot be smaller than the min value.
        self.assertRaises(ValueError, Range, 11, 5)

    def test_min(self):
        # The min attribute gives the minimum value in the Range.
        self.assertEqual(self.range.min(), 5)

    def test_max(self):
        # The max attribute gives the maximum value in the Range.
        self.assertEqual(self.range.max(), 11)

    def test_explicit(self):
        # Explicit returns the Range with intermediary values.
        self.assertEqual(self.range.explicit(), [5, 6, 7, 8, 9, 10, 11])

    def test_size(self):
        # Size is the length of the explicit Range.
        self.assertEqual(self.range.size(), 7)

    def test_append(self):
        with self.assertRaises(AttributeError):
            self.range.append(1)

    def test_index_range(self):
        self.assertEqual(Range.index_range(np.array([1, 2, 3]), 0), Range(0, 2))


if __name__ == '__main__':
    unittest.main()

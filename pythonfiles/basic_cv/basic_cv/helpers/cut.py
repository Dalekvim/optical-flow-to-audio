import numpy as np
from basic_cv.basic_cv.helpers.limiters import limit_l
from basic_cv.basic_cv.helpers.range import Range


def cut(matrix: np.ndarray, range_1: Range, range_2: Range) -> np.ndarray:
    """
    :param matrix: A two by two matrix.
    :param range_1: The range of required values for the first index.
    :param range_2: The range of required values for the second index.
    :return: A two by two matrix.
    """
    size_range_1 = range_1.size()
    size_range_2 = range_2.size()

    # Constructs an empty matrix with a shape given by the size of the ranges.
    cut_matrix = np.empty((size_range_1, size_range_2))

    # The .explicit() method makes ranges explicit e.g. Range(1, 5) -> [1, 2, 3, 4, 5].
    # limit_l limits a list to a certain range.
    limited_range_1 = limit_l(range_1.explicit(), Range.index_range(matrix, 0))
    limited_range_2 = limit_l(range_2.explicit(), Range.index_range(matrix, 1))

    for i in range(size_range_1):
        for j in range(size_range_2):
            index_1 = limited_range_1[i]
            index_2 = limited_range_2[j]

            cut_matrix.itemset((i, j), matrix.item((index_1, index_2)))

    return cut_matrix

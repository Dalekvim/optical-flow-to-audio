import numpy as np
from basic_cv.basic_cv.helpers.limiters import limit_i
from basic_cv.basic_cv.helpers.range import Range


def extend(matrix: np.ndarray, pos: tuple):
    """
    If the index is out of range this function returns the closest value.

    :param matrix: A matrix.
    :param pos: Index as a tuple.
    :return: Value of the matrix close to that index.
    """
    new_pos = list(pos)

    # Limits position values to within the matrix.
    for i in range(len(pos)):
        _range = Range.index_range(matrix, i)

        # Cannot use limit_l since different indices have different ranges.
        new_pos[i] = limit_i(pos[i], _range)

    return matrix.item(tuple(new_pos))

import numpy as np


def limit_i(integer, _range):
    """
    :param integer: Takes an integer.
    :param _range: Range in which the output should be contained.
    :return: The closest integer to the first argument that is in the range.
    """
    if not isinstance(integer, int):
        raise TypeError("The first argument for limit_i must be an integer.")
    if integer < _range[0]:
        return _range[0]
    elif integer > _range[-1]:
        return _range[-1]
    else:
        return integer


def limit_l(_list, _range):
    new_list = _list
    for i in range(len(_list)):
        new_list[i] = limit_i(_list[i], _range)
    return new_list


def extend(matrix, pos):
    """
    :param matrix: A two by two matrix.
    :param pos: Index as a tuple of length two.
    :return: Value of the matrix close to that index.
    """
    new_pos = list(pos)
    for i in range(len(pos)):
        new_pos[i] = limit_i(pos[i], [0, matrix.shape[i] - 1])
    return matrix.item(tuple(new_pos))


def length(_range):
    return _range[-1] - _range[0] + 1


def explicit_range(_range):
    return list(range(_range[0], _range[-1] + 1))


def cut(matrix, range_1, range_2):
    # Calculates Max - Min of the ranges.
    size_range_1 = length(range_1)
    size_range_2 = length(range_2)

    # Constructs a zero matrix using those values.
    cut_matrix = np.zeros((size_range_1, size_range_2))

    # Makes ranges explicit e.g. [1, 5] -> [1, 2, 3, 4, 5].
    # And limits them to a certain range.
    range_1 = limit_l(explicit_range(range_1), [0, matrix.shape[0] - 1])
    range_2 = limit_l(explicit_range(range_2), [0, matrix.shape[1] - 1])

    for i in range(size_range_1):
        for j in range(size_range_2):
            cut_matrix[i, j] = matrix[range_1[i], range_2[j]]

    return cut_matrix

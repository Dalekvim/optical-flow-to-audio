from basic_cv.basic_cv.helpers.range import Range


def limit_i(integer: int, _range: Range) -> int:
    """
    :param integer: Takes an integer.
    :param _range: Range in which the output should be contained.
    :return: The closest integer to the first argument that is in the range.
    """
    if not isinstance(integer, int):
        raise TypeError("The first argument for limit_i must be an integer.")
    if integer < _range.min():
        return _range.min()
    elif integer > _range.max():
        return _range.max()
    else:
        return integer


def limit_l(_list: list[int], _range: Range) -> list[int]:
    """
    :param _list: Takes a list of integers.
    :param _range: Range in which the integers should be contained.
    :return: Element is assigned the closest integer in the range.
    """
    new_list = _list
    for i in range(len(_list)):
        new_list[i] = limit_i(_list[i], _range)
    return new_list

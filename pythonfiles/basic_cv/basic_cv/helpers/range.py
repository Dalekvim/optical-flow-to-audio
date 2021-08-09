import numpy as np


class Range(list):
    def __init__(self, _min: int, _max: int):
        if not (isinstance(_min, int) and isinstance(_max, int)):
            raise TypeError("Limits of range must be integers.")
        if _min > _max:
            raise ValueError("Second argument cannot be smaller than the first.")
        self.extend([_min, _max])

    def explicit(self) -> list:
        return list(range(self.min(), self.max() + 1))

    def size(self) -> int:
        return len(self.explicit())

    def min(self) -> int:
        return self[0]

    def max(self) -> int:
        return self[1]

    def append(self, item):
        raise AttributeError

    @staticmethod
    def index_range(matrix: np.ndarray, dimension: int):
        return Range(0, matrix.shape[dimension] - 1)

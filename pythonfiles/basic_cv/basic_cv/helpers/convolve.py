import numpy as np

from basic_cv.basic_cv.helpers.cut import cut
from basic_cv.basic_cv.helpers.range import Range


def convolve(image: np.ndarray, matrix: np.ndarray, size: int) -> np.ndarray:
    radius = (size - 1) // 2

    convolved_image = np.empty(image.shape)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            cut_image = cut(image, Range(i - radius, i + radius), Range(j - radius, j + radius))
            convolved_image[i, j] = np.sum(np.multiply(cut_image, matrix))

    return convolved_image

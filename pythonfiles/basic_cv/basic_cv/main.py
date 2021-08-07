import numpy as np
from basic_cv.basic_cv.helpers import cut


def convolve(image, matrix, size):
    radius_1 = int((size - 1) / 2)
    radius_2 = int((size - 1) / 2)
    convolved_image = np.zeros(image.shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            cut_image = cut(image, [i - radius_1, i + radius_1], [j - radius_2, j + radius_2])
            convolved_image[i, j] = np.sum(np.multiply(cut_image, matrix))
    return convolved_image

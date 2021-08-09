import cv2
import numpy as np


class Kernel:
    """
    Quick access to basic kernels.

    Blur - This has two main types; "mean", which return a kernel of ones and "gaussian", which returns a kernel that
    is gaussian distributed horizontally and vertically with a maximum at the center.
    """

    @staticmethod
    def blur(dimensions: tuple, _type="mean") -> np.ndarray:
        if _type == "mean":
            ones = np.ones(dimensions)
            return ones / ones.size()
        elif _type == "gaussian":
            return cv2.getGaussianKernel(dimensions)

    @staticmethod
    def edge(_type="sobel_x") -> np.ndarray:
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

        if _type == "sobel_x":
            return sobel_x
        elif _type == "sobel_y":
            return sobel_x.T

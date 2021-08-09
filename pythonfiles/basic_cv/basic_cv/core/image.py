import cv2
import matplotlib.pyplot as plt

import numpy as np

from urllib.request import urlopen


class Image:
    """
    This class for controlling images files in OpenCV.
    """

    def __init__(self, name: str, np_array=None, path="", url=""):
        self.name = name

        if np_array is not None:
            self.as_array = np_array
        elif url:
            request = urlopen(url)
            array = np.asarray(bytearray(request.read()))
            self.as_array = cv2.imdecode(array, -1)
        elif path:
            self.as_array = cv2.imread(path)
        else:
            raise ValueError("No image input.")

        self.shape = self.as_array.shape

    def blur(self, dimensions: tuple, _type="mean") -> np.ndarray:
        if _type == "mean":
            return cv2.blur(self.as_array, dimensions)
        if _type == "gaussian":
            return cv2.GaussianBlur(self.as_array, dimensions, 0)

    def convolve(self, kernel) -> np.ndarray:
        return cv2.filter2D(self.as_array, -1, kernel)

    # TODO:
    #  1. Colour to grey scale.
    #  2. Gaussian blur.
    #  3. Edge detect.
    def edges(self):
        gray_image = Image("Gray Image", self.gray())
        blurred_gray = gray_image.blur((3, 3), _type="gaussian")
        return cv2.Sobel(blurred_gray, -1, 1, 1)

    def gray(self):
        return cv2.cvtColor(self.as_array, cv2.COLOR_BGR2GRAY)

    def save(self, filename):
        cv2.imwrite(filename, self.as_array)

    def show(self) -> None:
        cv2.imshow(self.name, self.as_array)

    def show_blur(self, _type) -> None:
        cv2.imshow(self.name, self.blur(_type))

    def show_edges(self) -> None:
        cv2.imshow(self.name, self.edges())

    def show_gray(self) -> None:
        cv2.imshow(self.name, self.gray())

    def plot(self) -> None:
        plt.imshow(self.as_array)

    def resize(self, dimensions: tuple) -> None:
        self.as_array = cv2.resize(self.as_array, dimensions)

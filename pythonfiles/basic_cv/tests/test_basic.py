import numpy as np

from basic_cv.basic_cv.helpers import extend

# Testing the extend function
one_to_three = np.array([x for x in range(9)]).reshape((3, 3))

# Normal values
for i in range(0, one_to_three.shape[0]):
    for j in range(0, one_to_three.shape[1]):
        assert extend(one_to_three, (i, j)) == 3 * i + j

# Extreme values
assert extend(one_to_three, (-1, -1)) == 0
assert extend(one_to_three, (3, 3)) == 8

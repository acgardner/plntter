import numpy as np


class Vector:

    def to_skew_mat(self, vec: Vector) -> np.array:
        """
        This function returns the 3x3 cross product matrix for a given 3-vector.
        """
        mat = np.array([[0, -vec[2], vec[1]],
                        [vec[2], 0, -vec[0]],
                        [-vec[1], vec[0], 0]])
        return mat

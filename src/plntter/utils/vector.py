from typing import Iterable

import numpy as np


class Vector:
    def __init__(self, vec: Iterable):
        if isinstance(vec, np.ndarray):
            self._vec = vec.flatten()
        if isinstance(vec, list):
            self._vec = np.array(vec)

    @property
    def val(self):
        return self._vec
    @val.setter
    def val(self, vec):
        self._vec = vec
    @property
    def x(self):
        return self._vec[0]
    @x.setter
    def x(self, val):
        self.x = val
    @property
    def y(self):
        return self._vec[1]
    @y.setter
    def y(self, val):
        self.y = val
    @property
    def z(self):
        return self._vec[2]
    @z.setter
    def z(self, val):
        self.z = val

    def to_skew_mat(self, dim=3) -> np.array:
        """
        This function generates a cross product matrix of size dim for a given 3-vector.
        """
        if dim == 3:
            mat = np.array([[0, -self.z, self.y],
                            [self.z, 0, -self.x],
                            [-self.y, self.x, 0]])
        if dim == 4:
            mat = np.array([[0, self.z, -self.y, self.x],
                            [-self.z, 0, self.x, self.y],
                            [self.y, -self.x, 0, self.z],
                            [-self.x, -self.y, -self.z, 0]])
        return mat

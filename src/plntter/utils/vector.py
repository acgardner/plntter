from __future__ import annotations
from typing import Iterable

import numpy as np


class Vector:
    def __init__(self, vec: Iterable) -> None:
        if isinstance(vec, np.ndarray):
            self._vec = vec.flatten()
        if isinstance(vec, list):
            self._vec = np.array(vec)

    @property
    def val(self) -> Vector:
        return self._vec
    @val.setter
    def val(self, vec: Iterable) -> Vector:
        self._vec = Vector(vec)
    @property
    def x(self) -> float:
        return self._vec[0]
    @x.setter
    def x(self, var: float) -> float:
        self.x = var
    @property
    def y(self) -> float:
        return self._vec[1]
    @y.setter
    def y(self, var: float) -> float:
        self.y = var
    @property
    def z(self) -> float:
        return self._vec[2]
    @z.setter
    def z(self, var: float) -> float:
        self.z = var
    
    def __add__(self, other: Vector) -> Vector:
        vec = []
        for it,num in enumerate(other.val):
            vec.append(self.val[it] + num)
        return Vector(vec)
    
    def __iadd__(self, other: Vector) -> Vector:
        vec = []
        for it,num in enumerate(other.val):
            vec.append(self.val[it] + num)
        return Vector(vec)

    def __sub__(self, other: Vector) -> Vector:
        vec = []
        for it,num in enumerate(other.val):
            vec.append(self.val[it] - num)
        return Vector(vec)

    def __isub__(self, other: Vector) -> Vector:
        vec = []
        for it,num in enumerate(other.val):
            vec.append(self.val[it] - num)
        return Vector(vec)

    def __matmul__(self, other: Vector) -> float:
        val = 0
        for it,num in enumerate(other.val):
            val += self.val[it]*num
        return val

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

    @staticmethod
    def random() -> Vector:
        ang_in_plane = np.random.uniform(0.,2.*np.pi)
        ang_out_of_plane = np.random.uniform(-np.pi,np.pi)
        vec = np.array((np.cos(ang_in_plane)*np.cos(ang_out_of_plane),
                        np.sin(ang_in_plane)*np.cos(ang_out_of_plane),
                        np.sin(ang_out_of_plane)))
        return Vector(vec)

    @staticmethod
    def norm(vec) -> float:
        """
        This function determines the scalar norm for a given 3-vector.
        """
        sum_of_squares = 0.
        for num in vec:
            sum_of_squares += num**2
        return np.sqrt(sum_of_squares)

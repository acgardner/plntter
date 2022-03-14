import numpy as np

from typing import Iterable
from .vector import Vector


class Quaternion:
    """
    Quaternion utility class
    q = [qv,q0]
    """
    def __init__(self, quat):
        self._quat = quat
        self._qv = self._quat[0:3]
        self._q0 = self._quat[-1]

    @property
    def val(self):
        return self._quat
    @val.setter
    def val(self, quat: Iterable):
        self._quat = quat
    @property
    def qv(self):
        return self._qv
    @qv.setter
    def qv(self, vec: Iterable):
        self._qv = Vector(vec).val
    @property
    def qx(self):
        return self.qv[0]
    @property
    def qy(self):
        return self.qv[1]
    @property
    def qz(self):
        return self.qv[2]
    @property
    def q0(self):
        return self._q0
    @q0.setter
    def q0(self, val: float):
        self._q0 = val

    def __mul__(self, p: Iterable):
        p = Quaternion(p)
        q = np.array([self.q0*p.q0 - self.qx*p.qx - self.qy*p.qy + self.qz*p.qz,
                      self.q0*p.qx + self.qx*p.q0 + self.qy*p.qz - self.qz*p.qy,
                      self.q0*p.qy - self.qx*p.qz + self.qy*p.q0 + self.qz*p.qx,
                      self.q0*p.qz + self.qx*p.qy - self.qy*p.qx + self.qz*p.q0])
        return q

    def to_mat(self) -> np.array:
        """
        This function computes the matrix equivalent of a given quaternion, q = [qv,q0].
        The matrix is a homogoneous quadratic function of q, and is orthogonal iff q has unit norm.
        """
        mat = np.eye(3)*(self.q0**2-np.abs(self.qv**2)) + 2.*self.qv*self.qv.T - 2.*self.q0*Vector.to_skew_mat(self.qv)
        return mat

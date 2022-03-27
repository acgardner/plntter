from __future__ import annotations
from typing import Iterable

from .vector import Vector

import numpy as np


class Quaternion:
    """
    Quaternion utility class
    q = [qv,q0]
    """
    def __init__(self, quat: Iterable) -> None:
        if isinstance(quat, np.ndarray):
            self._quat = quat.flatten()
        if isinstance(quat, list):
            self._quat = np.array(quat)
        self._qv = self._quat[0:3]
        self._q0 = self._quat[-1]

    @property
    def val(self) -> Quaternion:
        return self._quat

    @val.setter
    def val(self, quat: Iterable) -> Quaternion:
        self._quat = Quaternion(quat)

    @property
    def qv(self) -> Vector:
        return self._qv

    @qv.setter
    def qv(self, vec: Iterable) -> Vector:
        self._qv = Vector(vec).val

    @property
    def qx(self) -> float:
        return self.qv[0]

    @property
    def qy(self) -> float:
        return self.qv[1]

    @property
    def qz(self) -> float:
        return self.qv[2]

    @property
    def q0(self) -> float:
        return self._q0

    @q0.setter
    def q0(self, val: float) -> float:
        self._q0 = val

    def __mul__(self, p: Quaternion) -> Quaternion:
        q = np.array([self.q0*p.q0 - self.qx*p.qx - self.qy*p.qy + self.qz*p.qz,
                      self.q0*p.qx + self.qx*p.q0 + self.qy*p.qz - self.qz*p.qy,
                      self.q0*p.qy - self.qx*p.qz + self.qy*p.q0 + self.qz*p.qx,
                      self.q0*p.qz + self.qx*p.qy - self.qy*p.qx + self.qz*p.q0])
        return Quaternion(q)

    def __imul__(self, p: Quaternion) -> Quaternion: 
        q = np.array([self.q0*p.q0 - self.qx*p.qx - self.qy*p.qy + self.qz*p.qz,
                      self.q0*p.qx + self.qx*p.q0 + self.qy*p.qz - self.qz*p.qy,
                      self.q0*p.qy - self.qx*p.qz + self.qy*p.q0 + self.qz*p.qx,
                      self.q0*p.qz + self.qx*p.qy - self.qy*p.qx + self.qz*p.q0])
        return Quaternion(q)

    def inv(self) -> Quaternion:
        q = self.val
        q[0:3] *= -1.
        return Quaternion(q)

    def norm(self) -> Quaternion:
        self.val /= np.linalg.norm(self.val)

    def to_mat(self) -> np.array:
        """
        This function computes the matrix equivalent of a given quaternion, q = [qv,q0].
        The matrix is a homogeneous quadratic function of q, and is orthogonal iff q has unit norm.
        """
        mat = np.eye(3)*(self.q0**2-np.abs(self.qv**2)) + 2.*self.qv@self.qv.T - 2.*self.q0*Vector.to_skew_mat(self.qv)
        return mat

    def to_euler(self):
        """
        This function parameterizes a quaternion using an Euler angle and axis.
        """
        ang = 2.*np.arccos(self.q0)
        ax = self.qv / np.sin(ang/2.)
        return Vector(ax).val, ang

    @staticmethod
    def random(var: float) -> Quaternion:
        quat = Quaternion([0.,0.,0.,0.])

        ax = Vector.random()
        ang = np.random.normal(scale=np.sqrt(var))
        
        quat.qv = ax*np.sin(ang/2.)
        quat.q0 = np.cos(ang/2.)
        return quat

from .quaternion import Quaternion
from .vector import Vector

import numpy as np


class AttitudeKinematics:
    def __init__(self, q: Quaternion):
        self.q = q
    
    def propagate(self):
        pass

class AttitudeSolver:
    @staticmethod
    def QMethod(B: np.array, R: np.array, var: float) -> Quaternion:
        weight = 1./var
        weight /= np.sum(weight)
        A = np.dot(B,R.T*weight)
        z = np.array((A[1,2]-A[2,1],
                      A[2,0]-A[0,2],
                      A[0,1]-A[1,0])).reshape((3,1))
        K = np.block([
            [A+A.T-np.trace(A)*np.eye(3), z           ],
            [z.T,                         np.trace(A) ]
        ])
        w,v = np.linalg.eig(K)
        idx = np.argmax(w)
        return Quaternion(v[:,idx])

    def QUEST(self, r, b, var):
        pass

    def ESOQ(self, r, b, var):
        pass

    def ESOQ2(self, r, b, var):
        pass

    def TRIAD(self, r, b):
        pass

class AttitudeTransform:
    def __init__(self, transform_type: str) -> None:
        self.transform_type = transform_type

    def euler_to_mat(self, vec: Vector, ang: float) -> np.array:
        mat = np.eye(3)*np.cos(ang) + (1.-np.cos(ang))*vec.reshape((3,1))*vec.reshape((3,1)).T + vec.to_skew_mat()*np.sin(ang)
        return mat

    @staticmethod
    def arcsec_to_deg(val: float) -> float:
        return val / 3600.

    @staticmethod
    def arcsec_to_rad(val: float) -> float:
        return (val*np.pi) / (3600.*180.)
    
    @staticmethod
    def deg_to_arcsec(val: float) -> float:
        return val * 3600.

    @staticmethod
    def deg_to_rad(val: float) -> float:
        return val / 180.

    @staticmethod
    def rad_to_arcsec(val: float) -> float:
        return (val*180.*3600.) / np.pi

    @staticmethod
    def rad_to_deg(val: float) -> float:
        return (val*180.) / np.pi


from .quaternion import Quaternion
from .vector import Vector

import numpy as np


class AttitudeKinematics:
    def __init__(self, true_quat: Quaternion):
        self.true_quat = true_quat
    
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
    @staticmethod
    def euler_to_mat(ax: Vector, ang: float) -> np.array:
        """
        This function converts an Euler axis and angle to an attitude matrix
        """
        ax = np.reshape((3,1))
        return np.eye(3)*np.cos(ang) + (1.-np.cos(ang))*ax*ax.T + ax.to_skew_mat()*np.sin(ang)
    
    @staticmethod
    def euler_to_quat(ax: Vector, ang: float) -> Quaternion:
        """
        This function converts an Euler axis and angle to a quaternion
        """
        quat = Quaternion([0.,0.,0.,0.])
        quat.qv = ax*np.sin(ang/2.)
        quat.q0 = np.cos(ang/2.)
        return quat

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


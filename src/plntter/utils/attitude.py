from .quaternion import Quaternion
from .vector import Vector

class AttitudeKinematics:
    def __init__(self, q: Quaternion):
        self.q = q
    
    def propagate(self):
        pass

class AttitudeEstimator:
    def q_method(self, r, b, var):
        pass

    def QUEST(self, r, b, var):
        pass

    def ESOQ(self, r, b, var):
        pass

    def ESOQ2(self, r, b, var):
        pass

    def TRIAD(self, r, b):
        pass

    def euler_to_mat(self, vec: Vector, ang: float) -> np.array:
        mat = np.eye(3)*np.cos(ang) + (1.-np.cos(ang))*vec.reshape((3,1))*vec.reshape((3,1)).T + vec.to_skew_mat()*np.sin(ang)
        return mat

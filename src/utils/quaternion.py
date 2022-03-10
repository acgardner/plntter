import numpy as np

from plntter.src.utils.vector import Vector

class Quaternion:
    def to_mat(self, quat: Quaternion) -> np.array:
        """
        This function computes the matrix equivalent of a given quaternion, q = [qv,q0].
        The matrix is a homogoneous quadratic function of q, and is orthogonal iff q has unit norm.
        """
        mat = np.eye(3)*(quat.q0**2-np.abs(quat.qv**2)) + 2.*quat.qv*quat.qv.T - 2.*quat.q0*Vector.to_skew_mat(quat.qv)
        return mat

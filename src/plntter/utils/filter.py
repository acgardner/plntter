from .quaternion import Quaternion
from .vector import Vector

import numpy as np


class AEKF:
    """
    Placeholder class for Additive EKF
    """
    def predict(self):
        pass
    def update(self):
        pass

class MEKF:
    def __init__(self, state: np.array) -> None:
        self.state = state
        # error state vector = [3-vector of error angles, other 3-vector error states]
        # formal state vector = [4-element attitude quaternion, other 3-vector states]
    
    def predict(self) -> np.array:
        #x_k = f(x_km1) + w_k, w_k ~ N(0,Q_k)
        #x_k = f(q_km1,x_km1)
        #q_k = dq(dtheta_k) * q_km1
        #F_k = dfdx(q_km1,x_km1)
        #P_k = np.linalg.multi_dot((F_k,P_km1,F_k.T)) + Q_k
        pass

    def update(self) -> np.array:
        #z_k = h(x_k) + v_k, v_k ~ N(0,R_k)
        #H_k = dhdx(q_k,x_k)
        #S_k = np.linalg.multi_dot((H_k,P_k,H_k.T)) + R_k
        #K_k = np.linalg.multi_dot((P_k,H_k.T,np.linalg.inv(S_k)))
        #x_k = x_k + np.dot(K_k,(z_k-h(x_k)))
        #q_k = dq(dtheta_k) * q_km1
        #dq(dtheta_k) = np.array((dtheta_k,1)) / np.sqrt(1.+np.dot(dtheta_k.T,dtheta_k))
        #P_k = np.linalg.inv(np.linalg.inv(P_k)+np.linalg.multi_dot(H_k.T,np.linalg.inv(R),H_k))
        pass

class UKF:
    """
    Placeholder class for Unscented KF
    """
    def predict(self):
        pass
    def update(self):
        pass

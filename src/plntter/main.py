from plntter.utils.filters import AEKF, MEKF, UKF
from plntter.utils.vector import Vector
from plntter.utils.quaternion import Quaternion

vec = Vector([1,2,3])
quat = Quaternion([0,0,0,1])
kf = MEKF()

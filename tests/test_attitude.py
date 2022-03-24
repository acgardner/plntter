from plntter.utils.attitude import AttitudeSolver, AttitudeTransform
from plntter.utils.vector import Vector

import numpy as np


def test_QMethod() -> None:
    r1,r2,r3 = Vector.random(), Vector.random(), Vector.random()
    b1,b2,b3 = Vector.random(), Vector.random(), Vector.random()
    R,B = np.vstack((r1,r2,r3)), np.vstack((b1,b2,b3))
    var = AttitudeTransform.arcsec_to_rad(10)
    q = AttitudeSolver.QMethod(B,R,var)
    print(q.val)

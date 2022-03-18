import numpy as np

from plntter.utils.quaternion import Quaternion


def test_quat_setters() -> None:
    q = [0,0,0,1]
    qv = q[0:3]
    q0 = q[-1]
    quat = Quaternion(q)
    np.testing.assert_array_equal(quat.val, q)
    np.testing.assert_array_equal(quat.qv, qv)
    assert(quat.qx == qv[0])
    assert(quat.qy == qv[1])
    assert(quat.qz == qv[2])
    assert(quat.q0 == q0)

def test_quat_mult() -> None:
    q = Quaternion([1,0,0,1])
    p = [0,1,0,1]
    quat = q*p
    assert(type(quat) == Quaternion)
    np.testing.assert_array_equal(quat.val, [1,1,1,1])

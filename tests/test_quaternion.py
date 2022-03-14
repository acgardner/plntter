import numpy as np

from plntter.src.plntter.utils.quaternion import Quaternion


def test_quat_setters():
    q = [0,0,0,1]
    qv = q[0:3]
    q0 = q[-1]
    quat = Quaternion(q)
    assert quat.val == q
    assert quat.qv == qv
    assert quat.qx == qv[0]
    assert quat.qy == qv[1]
    assert quat.qz == qv[2]
    assert quat.q0 == q0

def test_quat_mult():
    q = Quaternion([1,0,0,1])
    p = [0,1,0,1]
    out = [1,1,1,1]
    np.testing.assert_array_equal(out, q*p)

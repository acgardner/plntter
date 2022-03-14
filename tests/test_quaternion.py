import numpy as np

from plntter.src.utils.quaternion import Quaternion


def test_quat_setter():
    q = [0,0,0,1]
    qv = [0,0,0]
    q0 = 1
    quat = Quaternion(q)
    assert quat.val == q
    assert quat.qv == qv
    assert quat.q0 == q0

def test_quat_mult():
    q = Quaternion([1,0,0,1])
    p = [0,1,0,1]
    out = [1,1,1,1]
    np.testing.assert_array_equal(out, q*p)

from plntter.src.utils.vector import Vector

import numpy as np


def test_vec_setter():
    x = np.array([1,2,3])
    x_vec = Vector([1,2,3]).val
    np.testing.assert_array_equal(x, x_vec)

def test_skew_size():
    x_vec = Vector([1,2,3])
    skew_mat3 = x_vec.to_skew_mat(dim=3)
    skew_mat4 = x_vec.to_skew_mat(dim=4)
    assert skew_mat3.shape[0] == 3 and skew_mat3.shape[1] == 3
    assert skew_mat4.shape[0] == 4 and skew_mat4.shape[1] == 4

def test_to_skew_mat3():
    x = [1,2,3]
    y = [4,5,6]
    cp_ref = np.cross(x,y)

    x_vec, y_vec = Vector(x), Vector(y).val
    cp_vec = np.dot(x_vec.to_skew_mat(dim=3), y_vec)
    np.testing.assert_array_equal(cp_ref, cp_vec)

def test_to_skew_mat4():
    pass

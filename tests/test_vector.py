import numpy as np

from plntter.utils.vector import Vector


def test_vec_setter() -> None:
    vec = np.array([1,2,3])
    vec_val = Vector([1,2,3]).val
    np.testing.assert_array_equal(vec, vec_val)

def test_skew_size() -> None:
    vec = Vector([1,2,3])
    skew_vec3 = vec.to_skew_mat(dim=3)
    skew_vec4 = vec.to_skew_mat(dim=4)
    assert (skew_vec3.shape[0] == 3 and skew_vec3.shape[1] == 3)
    assert (skew_vec4.shape[0] == 4 and skew_vec4.shape[1] == 4)

def test_to_skew_mat3() -> None:
    x = [1,2,3]
    y = [4,5,6]
    z = np.dot(Vector(x).to_skew_mat(dim=3), Vector(y).val)
    sol = np.cross(x, y)
    np.testing.assert_array_equal(z, sol)

def test_to_skew_mat4() -> None:
    pass

def test_add_two_vectors():
    tests = [
        [[1],[1]],
        [[1,2],[2,1]],
        [[1,2,3],[3,2,1]]
    ]
    sols = [
        [2],
        [3,3],
        [4,4,4]
    ]
    x = Vector([1,2,3])
    y = Vector([3,2,1])
    z = x.val + y.val
    for t,s in zip(tests,sols):
        x, y = Vector(t[0]), Vector(t[1])
        z = x.val + y.val
        np.testing.assert_array_equal(z, s)

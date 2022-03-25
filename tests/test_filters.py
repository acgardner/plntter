from plntter.utils.attitude import AttitudeTransform
from plntter.utils.filter import AEKF, MEKF, UKF
from plntter.utils.quaternion import Quaternion
from plntter.utils.sensors import IMU, StarTracker
from plntter.utils.vector import Vector

import numpy as np


def test_MEKF() -> None:
    true_quat = Quaternion([0.,0.,1.,0.])
    true_w = Vector([0.,0.,0.])
    true_wbias = Vector([0.,0.,AttitudeTransform.deg_to_rad(0.1)])
    true_state = np.hstack((true_quat.val, true_wbias.val))

    imu = IMU(true_w)
    star_tracker = StarTracker()

    mekf = MEKF(true_state)
    pred = mekf.predict()
    updt = mekf.update()

def test_UKF() -> None:
    ukf = UKF()
    pred = ukf.predict()
    updt = ukf.update()

from plntter.utils.plotter import Plotter
from plntter.utils.sensors import IMU
from plntter.utils.vector import Vector

import matplotlib.pyplot as plt
import numpy as np


def test_IMU():
    w_true = Vector([0.,0.,0.])
    gyro_err = {
        "sampling_freq": 200.,
        "bias_model": "gauss_markov",
        "correlation_time": 100.,
        "bias_var": np.deg2rad(0.1),
        "sensor_var": np.deg2rad(0.01)
    }
    sample_time = [sample for sample in range(101)]
    w_meas = np.zeros((3, len(sample_time)))
    imu = IMU(w_true, gyro_err)
    for sample in sample_time:
        w_meas[:,sample] = imu.get_measurement()
    
    plot_params = {
        "type": "lineplot",
        "xlabel": "Time (s)",
        "ylabel": "Angular Rate (deg/s)",
        "y_data_labels": [
            "x",
            "y",
            "z",
        ],
        "x_data": sample_time,
        "y_data": [
            w_meas[0,:],
            w_meas[1,:],
            w_meas[2,:],
        ],
    }
    p = Plotter(plot_params)

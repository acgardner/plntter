from plntter.utils.plotter import Plotter
from plntter.utils.sensors import IMU
from plntter.utils.vector import Vector

import matplotlib.pyplot as plt
import numpy as np


def test_IMU():
    freq = 400
    w_true = Vector([0.,0.,0.])
    gyro_err = {
        "sampling_freq": freq,
        "bias_model": "gauss_markov",
        "correlation_time": 100.,
        "bias_var": np.deg2rad(0.1),
        "sensor_var": np.deg2rad(0.01)
    }
    time = np.linspace(0,60,freq)    
    w_meas = np.zeros((3,len(time)))
    imu = IMU(w_true,gyro_err)
    for dt,_ in enumerate(time):
        w_meas[:,dt] = imu.get_measurement()

    plot_params = {
        "type": "lineplot",
        "xlabel": "Time (s)",
        "ylabel": "Angular Rate (deg/s)",
        "y_data_labels": [
            "x",
            "y",
            "z",
        ],
        "x_data": time,
        "y_data": [
            w_meas[0,:],
            w_meas[1,:],
            w_meas[2,:],
        ],
    }
    #p = Plotter(plot_params)

from .vector import Vector

import numpy as np


class IMU:
    def __init__(self, w_true: Vector, gyro_err: dict) -> None:
        self.w_true = w_true.val
        self.gyro_err = gyro_err
        self.bias = Vector([0.,0.,0.]).val
        self.dt = 1. / self.gyro_err["sampling_freq"]

    def apply_bias(self) -> Vector:
        if self.gyro_err["bias_model"] == "random_walk":
            bias_x = self.bias[0] + np.random.normal(0., np.sqrt(self.gyro_err["bias_var"]))
            bias_y = self.bias[1] + np.random.normal(0., np.sqrt(self.gyro_err["bias_var"]))
            bias_z = self.bias[2] + np.random.normal(0., np.sqrt(self.gyro_err["bias_var"]))
            self.bias = Vector([bias_x, bias_y, bias_z]).val
        elif self.gyro_err["bias_model"] == "gauss_markov":
            Tc = self.gyro_err["correlation_time"]
            bias_x = np.exp(-self.dt/Tc)*self.bias[0] + np.random.normal(0., np.sqrt(self.gyro_err["bias_var"]))
            bias_y = np.exp(-self.dt/Tc)*self.bias[1] + np.random.normal(0., np.sqrt(self.gyro_err["bias_var"]))
            bias_z = np.exp(-self.dt/Tc)*self.bias[2] + np.random.normal(0., np.sqrt(self.gyro_err["bias_var"]))
            self.bias = Vector([bias_x, bias_y, bias_z]).val
        else:
            pass
        return self.bias

    def get_measurement(self) -> Vector:
        bias = self.apply_bias()
        w_meas_x = self.w_true[0] + bias[0] + np.random.normal(0., np.sqrt(self.gyro_err["sensor_var"]))
        w_meas_y = self.w_true[1] + bias[1] + np.random.normal(0., np.sqrt(self.gyro_err["sensor_var"]))
        w_meas_z = self.w_true[2] + bias[2] + np.random.normal(0., np.sqrt(self.gyro_err["sensor_var"]))
        w_meas = Vector([w_meas_x, w_meas_y, w_meas_z]).val
        return w_meas

class Inclinometer:
    def __init__(self):
        self.x = []

class RangeSensor:
    def __init__(self):
        self.x = []

class StarTracker:
    def __init__(self):
        self.x = []

class SunSensor:
    def __init__(self):
        self.x = []

from .attitude import AttitudeTransform
from .quaternion import Quaternion
from .vector import Vector

import numpy as np


class IMU:
    """
    w_meas = w_true + bias + white_noise
    """
    def __init__(self,
                 w_true: Vector,
                 gyro_err: dict={
                     "bias_model": "no_bias",
                     "sampling_freq": 1.,
                     "bias_var": 0.,
                     "sensor_var": 0.,
                     }
                 ) -> None:
        self.w_true = w_true.val
        self.gyro_err = gyro_err
        self.bias = Vector([0.,0.,0.]).val
        self.dt = 1. / self.gyro_err["sampling_freq"]

    def apply_bias(self) -> Vector:
        if self.gyro_err["bias_model"] == "random_walk":
            bias_x = self.bias[0] + np.random.normal(loc=np.sqrt(self.gyro_err["bias_var"]))
            bias_y = self.bias[1] + np.random.normal(loc=np.sqrt(self.gyro_err["bias_var"]))
            bias_z = self.bias[2] + np.random.normal(loc=np.sqrt(self.gyro_err["bias_var"]))
            self.bias = Vector([bias_x, bias_y, bias_z]).val
        elif self.gyro_err["bias_model"] == "gauss_markov":
            Tc = self.gyro_err["correlation_time"]
            bias_x = np.exp(-self.dt/Tc)*self.bias[0] + np.random.normal(loc=np.sqrt(self.gyro_err["bias_var"]))
            bias_y = np.exp(-self.dt/Tc)*self.bias[1] + np.random.normal(loc=np.sqrt(self.gyro_err["bias_var"]))
            bias_z = np.exp(-self.dt/Tc)*self.bias[2] + np.random.normal(loc=np.sqrt(self.gyro_err["bias_var"]))
            self.bias = Vector([bias_x, bias_y, bias_z]).val
        elif self.gyro_err["bias_model"] == "no_bias":
            bias_x = 0.
            bias_y = 0.
            bias_z = 0.
            self.bias = Vector([bias_x, bias_y, bias_z]).val
        return self.bias

    def get_measurement(self) -> Vector:
        bias = self.apply_bias()
        w_meas_x = self.w_true[0] + bias[0] + np.random.normal(loc=np.sqrt(self.gyro_err["sensor_var"]))
        w_meas_y = self.w_true[1] + bias[1] + np.random.normal(loc=np.sqrt(self.gyro_err["sensor_var"]))
        w_meas_z = self.w_true[2] + bias[2] + np.random.normal(loc=np.sqrt(self.gyro_err["sensor_var"]))
        w_meas = Vector([w_meas_x, w_meas_y, w_meas_z]).val
        return w_meas

class Inclinometer:
    def __init__(self):
        self.x = []

class RangeSensor:
    def __init__(self):
        self.x = []

class StarTracker:
    """
    b = T(q_bi)*r_i + white_noise
    """
    def __init__(self, params: dict={}) -> None:
        self._name = 'Star Tracker'

        if 'var' in params.keys():
            self._var = params['var']
        else:
            self._var = var=(np.deg2rad(10/3600))**2

        if 'vectorVar' in params.keys():
            self._vectorVar = params['vectorVar']
        else:
            self._vectorVar = vectorVar=(np.deg2rad(10/3600))**2

        if 'vectorMean' in params.keys():
            self._vectorMean = np.array(params['vectorMean'])
        else:
            self._vectorMean = vectorMean=np.array([[0.],[0.],[1.]])

        if 'minStars' in params.keys():
            self._minStars = params['minStars']
        else:
            self._minStars = minStars=5

        if 'maxStars' in params.keys():
            self._maxStars = params['maxStars']
        else:
            self._maxStars = maxStars=30

    def _num_meas(self) -> int:
        return int((np.random.rand()*(self._maxStars-self._minStars)+self._minStars))
    
    def get_measurement(self, true_quat: Quaternion):
        true_att_mat = true_quat.to_mat()
        num_meas = self._num_meas()
        R, B = np.zeros((3,num_meas)), np.zeros((3,num_meas))

        for meas in range(num_meas):
            if self._vectorMean is None:
                R[:,meas:meas+1] = Vector.random()
            else:
                e = np.expand_dims(np.cross(self._vectorMean, Vector.random()), axis=1)
                e /= np.linalg.norm(e)
                phi = np.random.normal(scale=np.sqrt(self._vectorVar))
                R[:,meas:meas+1] = np.dot(AttitudeTransform.euler_to_mat(e,phi), self._vectorMean)
        
        for meas in range(num_meas):
            true_meas_vec = np.dot(true_att_mat, R[:,meas])
            e = np.expand_dims(np.cross(true_meas_vec, Vector.random()), axis=1)
            e /= np.linalg.norm(e)
            phi = np.random.normal(scale=np.sqrt(self._var))
            B[:,meas] = np.dot(AttitudeTransform.euler_to_mat(e,phi), true_meas_vec)
        
        return R, B, np.ones((num_meas))*self._var

class SunSensor:
    def __init__(self):
        self.x = []

"""
Holds versions of the filter's state and error state vectors
"""

from .attitude import AttitudeTransform
from .quaternion import Quaternion
from .vector import Vector

import numpy as np

class TrajectoryGenerator:
    def ConstWVal(q1,q2,tf):
        """
        Calculate the angular velocity constant needed to move from one attitude quaternion to another.
        """
        qPert = q2*q1.inv()
        e,phi = qPert.to_euler()
        return e*phi/tf

    def ConstW(q1,q2,tf):
        """
        Returns a function of time for the constant angular velocity case.
        """
        w = TrajectoryGenerator.ConstWVal(q1,q2,tf)
        def outFunc(t,c):
            return w
        return outFunc

    def ConstQ(q1,q2,tf):
        """
        Returns a function for a perturbed quaternion (relative to the initial quaternion) for a constant angular velocity case.
        """
        w = TrajectoryGenerator.ConstWVal(q1,q2,tf)
        wnorm = np.linalg.norm(wnorm)
        ehat = w/np.linalg.norm(w)
        def outFunc(t,c):
            return AttitudeTransform.euler_to_quat(ehat,w*t)
        return outFunc


class StateAndGyroBias:
    def f(q,x,w,c):
        wEst = w-x[3:,0:1]
        qw = np.zeros(4)
        qw[1:] = 1./2.*wEst.flatten()*c['dt']
        qw = Quaternion(qw)
        dq = qw*q
        dark.val += q.val
        dark *= q.inv()
        out = np.copy(x)
        out[0:3,0:1] = dark.val[1:,0:1]*2.
        return out

    def fTrue(sim):
        qk = sim.qPertFunc(sim.c['t'],sim.c)
        qkm1 = sim.qPertFunc(sim.c['t']-sim.c['dt'],sim.c)
        dq = (qk*qkm1.inv()).val
        dq /= dq[0,0]

        bias = sim._propSensors['IMU']._gyroBias
        return np.vstack([dq[1:,0:1]*2.,bias])

    def h(q,x,c):
        return x[0:3,0:1]

    def hTrue(sim):
        qk = sim.qPertFunc(sim.c['t'],sim.c)
        qmk1 = sim.qPertFunc(sim.c['t']-sim.c['dt'],sim.c)
        dq = qk*qkm1.inv()
        qMeas = sim._propSensors['VisualOdometer'].GetMeasurement(dq)
        qMeas = qMeas.val
        return qMeas[1:,0:1]/qMeas[0,0]*2.

    def F(q,x,w,c):
        W = (w-x[3:,0:1])*c['dt']
        Z = np.zeros((3,3))
        return np.block([
            [AttitudeTransform.Skew(W)+np.eye(3), AttitudeTransform.Skew(x[0:3,0:1])*c['dt']],
            [Z,                                   np.eye(3)                                 ]
        ])



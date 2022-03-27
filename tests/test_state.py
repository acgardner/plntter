from plntter.utils.attitude import AttitudeTransform
from plntter.utils.plotter import Plotter
from plntter.utils.quaternion import Quaternion
from plntter.utils.state import TrajectoryGenerator
from plntter.utils.vector import Vector

import numpy as np


def test_trajectory_generator():
    q0 = Quaternion.random(np.pi)
    qf = Quaternion.random(np.pi)

    t0 = 0.
    tf = 3.
    dt = 0.1
    t = np.arange(t0,tf+dt,dt)
    wt = np.zeros((3,t.shape[0]))
    w = TrajectoryGenerator.ConstW(q0,qf,tf)
    for it,dt in enumerate(t):
        wt[:,it] = w(dt,0)
    print(wt)

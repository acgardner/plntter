from plntter.utils.filter import UKF
from plntter.utils.vector import Vector
from plntter.utils.quaternion import Quaternion
from plntter.utils.sensors import IMU, StarTracker

vec = Vector([1,2,3])
quat = Quaternion([0,0,0,1])
ukf = UKF()

imu = IMU()
st = StarTracker()

print(f"I ran! Here is proof: {imu.x}")

from plntter.src.plntter.utils.filters import AEKF, MEKF, UKF


def test_AEKF():
    aekf = AEKF()
    pred = aekf.predict()
    updt = aekf.update()

def test_MEKF():
    mekf = MEKF()
    pred = mekf.predict()
    updt = mekf.update()

def test_UKF():
    ukf = UKF()
    pred = ukf.predict()
    updt = ukf.update()

from plntter.utils.filters import AEKF, MEKF, UKF


def test_AEKF() -> None:
    aekf = AEKF()
    pred = aekf.predict()
    updt = aekf.update()

def test_MEKF() -> None:
    mekf = MEKF()
    pred = mekf.predict()
    updt = mekf.update()

def test_UKF() -> None:
    ukf = UKF()
    pred = ukf.predict()
    updt = ukf.update()

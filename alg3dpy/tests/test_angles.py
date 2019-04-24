from alg3dpy.angles import (cos2vecs, sin2vecs, sinplanevec, cosplanevec,
        angle2vecs, angle2planes, angleplanevec)
from alg3dpy.constants import PLANEXY, PLANEXZ, X, Y, Z

import numpy as np

def test_angles():
    assert angle2vecs(X, Y) == np.pi/2
    assert sin2vecs([2, 0, 0], [0, 1, 0]) == 1.
    assert cos2vecs([2, 0, 0], [0, 1, 0]) == 0.
    assert sinplanevec(PLANEXY, Z) == 1.
    assert cosplanevec(PLANEXY, Z) == 0.
    assert angle2planes(PLANEXY, PLANEXZ) == np.pi/2
    assert angleplanevec(PLANEXY, X) == 0
    assert angleplanevec(PLANEXY, Z) == np.pi/2

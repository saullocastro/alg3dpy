from numpy import pi, cos, isclose

from alg3dpy.angles import (cos2vecs, sin2vecs, sinplanevec, cosplanevec,
        angle2vecs, angle2planes, angleplanevec)
from alg3dpy.constants import PLANEXY, PLANEXZ, X, Y, Z

def test_angles():
    assert isclose(angle2vecs(X, Y), pi/2)
    assert isclose(sin2vecs([2, 0, 0], [0, 1, 0]), 1.)
    assert isclose(cos2vecs([2, 0, 0], [0, 1, 0]), 0.)
    assert isclose(sinplanevec(PLANEXY, Z), 1.)
    assert isclose(cosplanevec(PLANEXY, Z), 0.)
    assert isclose(angle2planes(PLANEXY, PLANEXZ), pi/2)
    assert isclose(angleplanevec(PLANEXY, X), 0)

    assert isclose(angleplanevec(PLANEXY, Z), pi/2)
    assert isclose(cosplanevec(PLANEXY, Z), cos(pi/2))

    assert isclose(angleplanevec(PLANEXY, -Z), -pi/2)
    assert isclose(cosplanevec(PLANEXY, -Z), cos(-pi/2))

    assert isclose(angleplanevec(PLANEXY, [1, 0, 1]), pi/4)
    assert isclose(cosplanevec(PLANEXY, [1, 0, 1]), cos(pi/4))

    assert isclose(angleplanevec(PLANEXY, [-1, 0, +1]), pi/4)
    assert isclose(cosplanevec(PLANEXY, [-1, 0, +1]), cos(pi/4))

    assert isclose(angleplanevec(PLANEXY, [-1, 0, -1]), -pi/4)
    print(angleplanevec(PLANEXY, [-1, 0, -1]))
    assert isclose(cosplanevec(PLANEXY, [-1, 0, -1]), cos(-pi/4))
    print(cosplanevec(PLANEXY, [-1, 0, -1]))

    assert isclose(angleplanevec(PLANEXY, [+1, 0, -1]), -pi/4)
    assert isclose(cosplanevec(PLANEXY, [+1, 0, -1]), cos(-pi/4))

    assert isclose(angleplanevec(PLANEXY, [+1, 0, -1]), -pi/4)
    assert isclose(cosplanevec(PLANEXY, [+1, 0, -1]), cos(-pi/4))

if __name__ == "__main__":
    test_angles()

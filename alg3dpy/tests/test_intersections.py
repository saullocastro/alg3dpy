import numpy as np

from alg3dpy.intersections import (intersectplaneline, intersect2lines)
from alg3dpy.constants import PLANEXY

def test_intersections():
    assert intersectplaneline(PLANEXY, [[1.5, 2.5, 1], [1.5, 2.5, 2]], False) is None
    assert np.allclose(intersectplaneline(PLANEXY, [[1.5, 2.5, 1], [1.5, 2.5, 2]], True), [1.5, 2.5, 0])
    assert intersect2lines([[2.5, 2.5, 1], [3.5, 2.5, 1]],
            [[1.5, 2.5, 1], [1.5, 2.5, 2]], False, False) is None
    assert np.allclose(intersect2lines([[2.5, 2.5, 1], [3.5, 2.5, 1]],
            [[1.5, 2.5, 1], [1.5, 2.5, 2]], True, False), [1.5, 2.5, 1])
    assert intersect2lines([[2.5, 2.5, 1], [3.5, 2.5, 1]],
            [[1.5, 2.5, 1], [1.5, 2.5, 2]], False, True) is None
    assert intersect2lines([[0, 1, 1], [0, 2, 2]],
            [[1, -1, -1], [1, -2, -2]], True, True) is None
    assert np.allclose(intersect2lines([[0, 1, 1], [0, 2, 2]],
            [[0, 2, 1], [0, 1, 2]], False, False), [0, 1.5, 1.5])
    assert np.allclose(intersect2lines([[0, 1, 1], [0, 2, 2]],
            [[0, -1, 1], [0, -2, 2]], True, True), [0, 0, 0])

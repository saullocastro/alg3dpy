import numpy as np

from alg3dpy.distances import (distplanept, distplaneplane, distplaneline,
        distptpt, distlinept, distlineline)
from alg3dpy.constants import PLANEXY
from alg3dpy.plane import plane1vec1pt


def test_distances():
    assert distplanept(PLANEXY, [0, 0, 2.5]) == 2.5
    offset = plane1vec1pt(PLANEXY.normal, [0, 0, 100])
    assert distplanept(offset, [0, 0, 2.5]) == -97.5
    assert distplanept(offset, [0, 0, 105.]) == 5.
    assert distplaneplane(PLANEXY, offset) == 100.
    line = np.array([[0, 0, 1.5], [0, 0, 2.]])
    assert distplaneline(PLANEXY, line, False) == 1.5
    assert distplaneline(PLANEXY, line, True) == 0
    assert distptpt([1, 1, 1], [-2, -2, -2]) == (3 * 3**2)**0.5
    assert distlinept([[1, 1, 1], [2, 2, 2]], [-2, -2, -2], False) == (3 * 3**2)**0.5
    assert distlinept([[1, 1, 1], [2, 2, 2]], [-2, -2, -2], True) == 0
    assert np.isclose(distlinept([[1, 1, 1], [2, 2, 2]], [0, 1, 0], True), 0.816496580927726)
    assert distlinept([[0, 1, 3], [0, 1, 5]], [0, 1, 0], False) == 3
    assert distlinept([[0, 1, 3], [0, 1, 5]], [0, 2, 0], True) == 1
    assert distlineline([[0, 0, 0], [0, 0, 1]], [[0, 1.5, 0], [0, 3, 0]], False,
            False) == 1.5
    assert distlineline([[0, 0, 1], [0, 0, 2]], [[0, 1.5, 0], [0, 3, 0]], True,
            False) == 1.5
    assert distlineline([[0, 0, 1], [0, 0, 2]], [[0, 1.5, 0], [0, 3, 0]], False,
            True) == 1
    assert distlineline([[0, 0, 1], [0, 0, 2]], [[0, 1.5, 0], [0, 3, 0]], True,
            True) == 0
    assert distlineline([[0, 0, 1], [0, 0, 2]], [[0, 1.5, 0], [0, 3, 0]], True,
            True) == 0


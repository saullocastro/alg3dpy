import numpy as np

from alg3dpy.areas import area_tria


def test_areas():
    assert np.isclose(area_tria([0, 2, 0], [2, 0, 0], [0, 0, 2]),
            3.4641016151377557)

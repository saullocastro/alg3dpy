import numpy as np

def test_plane():
    from alg3dpy.plane import plane3points, plane2lines
    from alg3dpy.line import asline
    from alg3dpy.vector import asvector
    YZneg = plane3points([0, 0, 0], [0, 0, 1], [0, 1, 0])
    line = asline([[1, 0, 0], [2, 0, 0]])
    assert YZneg.anglewith(line) == -np.pi/2
    line = asline([[-1, 0, 0], [-2, 0, 0]])
    assert YZneg.anglewith(line) == np.pi/2
    assert YZneg.anglewith(asvector([1, 0, 0])) == -np.pi/2
    assert YZneg.anglewith(asvector([-1, 0, 0])) == np.pi/2
    XZ = plane2lines([[0, 0, 0], [0, 0, 1]],
                     [[0, 0, 0], [1, 0, 0]])
    assert XZ.anglewith(YZneg) == np.pi/2
    assert YZneg.anglewith(XZ) == np.pi/2
    assert XZ.distfrom(YZneg) == 0
    assert XZ.distfrom([1, 0, 0]) == 0
    assert XZ.distfrom([0, 0, 1]) == 0
    assert XZ.distfrom([0, 2.5, 0]) == 2.5
    assert XZ.distfrom(asline([[0, 2.5, 0], [0, 3.5, 0]])) == 2.5
    assert XZ.distfrom(asline([[0, 2.5, 0], [0, 3.5, 0]]), extend_other=True) == 0

import numpy as np

def test_vector():
    from alg3dpy.line import asline
    from alg3dpy.vector import asvector
    from alg3dpy.plane import plane2lines
    xaxis = asvector([1, 0, 0])
    yaxis = asvector([0, 1, 0])
    zaxis = asvector([0, 0, 1])
    yaxisneg = asvector([0, -1, 0])
    assert xaxis.anglewith(yaxis) == np.pi/2
    assert yaxis.anglewith(xaxis) == np.pi/2
    XZ = plane2lines([[0, 0, 0], [0, 0, 1]],
                     [[0, 0, 0], [1, 0, 0]])
    assert yaxis.anglewith(XZ) == np.pi/2
    assert xaxis.anglewith(XZ) == 0
    line = asline([[1, 0, 0], [2, 0, 0]])
    line2 = asline([[-1, 0, 0], [-2, 0, 0]])
    assert xaxis.anglewith(line) == 0
    assert xaxis.anglewith(line2) == np.pi
    assert yaxis.anglewith(line) == np.pi/2
    assert yaxis.anglewith(line2) == np.pi/2
    assert xaxis.dot(yaxis) == 0
    assert xaxis.dot(xaxis) == 1
    v = asvector([1, 2, 3])
    assert np.allclose(v.norm(), v/np.linalg.norm(v))
    assert np.allclose(xaxis.cross(yaxis), zaxis)
    assert np.allclose(yaxis.cross(xaxis), -zaxis)


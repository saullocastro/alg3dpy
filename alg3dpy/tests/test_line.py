import numpy as np

def test_line():
    from alg3dpy.line import asline, ptinline
    from alg3dpy.plane import plane1vec1pt
    from alg3dpy.vector import asvector
    plane = plane1vec1pt([1, 0, 0], [5, 0, 0])
    a = asline([[0, 0, 0], [0, 1, 0]])
    check = a.extendto(plane, extend_other=False)
    assert not check
    a = asline([[0, 0, 0], [1, 1, 1]])
    pt = ptinline(a, 0.5)
    assert np.allclose(pt, [0.5, 0.5, 0.5])
    check = a.extendto(plane, extend_other=False)
    assert check # means that there is a valid intersection
    assert np.allclose(a.pt2, [5, 5, 5])
    a = asline([[0, 0, 0], [1, 1, 0]])
    b = asline([[-1, 0, 0], [-2, 1, 0]])
    intersc = a.intersect(plane, extend_me=True, extend_other=True)
    assert np.allclose(intersc, [5, 5, 0])
    intersc = a.intersect(plane, extend_me=False, extend_other=True)
    assert intersc is None
    intersc = a.intersect(b, extend_me=False, extend_other=True)
    assert intersc is None
    intersc = a.intersect(b, extend_me=True, extend_other=False)
    assert intersc is None
    intersc = a.intersect(b, extend_me=True, extend_other=True)
    assert intersc is not None
    assert np.allclose(intersc, [-0.5, -0.5, 0])
    a = asline([[0, 1, 0], [2, 1, 0]])
    b = asline([[10, 0, 0], [20, 0, 0]])
    dist = a.distfrom(b, extend_me=False, extend_other=False)
    assert np.allclose(dist, ((10-2)**2 + 1**2)**0.5)
    dist = a.distfrom(b, extend_me=True, extend_other=False)
    assert np.allclose(dist, 1)
    dist = a.distfrom(b, extend_me=False, extend_other=True)
    assert np.allclose(dist, 1)
    assert a.anglewith(b) == 0
    assert a.anglewith(asvector([0, 1, 0])) == np.pi/2
    assert a.anglewith(plane1vec1pt([0, 1, 0], [0, 0, 0])) == 0
    assert a.anglewith(plane1vec1pt([1, 0, 0], [0, 0, 0])) == np.pi/2



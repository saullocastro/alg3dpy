from __future__ import absolute_import

import numpy as np

class Vec(np.ndarray):
    """
    """
    uniqueid = 1
    def __array_finalize__(self, obj):
        self.id = Vec.uniqueid
        Vec.uniqueid += 1

    @property
    def i(self):
        return self[..., 0]

    @property
    def j(self):
        return self[..., 1]

    @property
    def k(self):
        return self[..., 2]

    def dot(self, vec2):
        if self.ndim >= 1 and vec2.ndim == 1:
            return np.dot(self, vec2)
        else:
            return np.tensordot(self, vec2, [[-1], [-1]])

    def norm(self):
        self /= np.linalg.norm(self)
        return self

    def cross(self, vec2):
        return np.cross(self, vec2).view(Vec).norm()

    def mod(self):
        return np.linalg.norm(self)

    def __str__(self):
        return 'Vector ID %d: %2.3f i + %2.3f j + %2.3f k'\
               % (self.id, self.i, self.j, self.k)

    def __repr__(self):
        return 'alg3dpy.Vec class'

    def anglewith(self, entity):
        from .angles import angleplanevec, angle2vecs, anglelinevec
        from .line import Line
        from .plane import Plane
        if isinstance(entity, Plane):
            return angleplanevec(entity, self)
        if isinstance(entity, Vec):
            return angle2vecs(self, entity)
        if isinstance(entity, Line):
            return anglelinevec(entity, self)

    def cosines_GLOBAL(self):
        from .constants import PLANEXY, PLANEXZ
        from .angle import cosplanevec
        cosbeta = cosplanevec(PLANEXY, self)
        cosgama = cosplanevec(PLANEXZ, self)
        return [cosbeta, cosgama]


def asvector(a):
    from .constants import FLOAT
    if isinstance(a, Vec):
        return a
    else:
        return np.asarray(a, dtype=FLOAT).view(Vec)


def ortvec3points(pt1, pt2, pt3):
    vec1 = pt2 - pt1
    vec2 = pt3 - pt1
    return np.cross(vec1, vec2).view(Vec).norm()


def ortvec2vecs(vec1, vec2):
    return np.cross(vec1, vec2).view(Vec).norm()

#Weisstein, Eric W. "Normalized Vector." From MathWorld--A Wolfram Web Resource.
#   http://mathworld.wolfram.com/NormalizedVector.html
#Weisstein, Eric W. "Norm." From MathWorld--A Wolfram Web Resource.
#   http://mathworld.wolfram.com/Norm.html

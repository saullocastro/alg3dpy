from __future__ import absolute_import

import numpy as np

class Point(np.ndarray):
    uniqueid = 1

    def __array_finalize__(self, obj):
        self.id = Point.uniqueid
        Point.uniqueid += 1

    def __init__(self):
        self.id = Point.uniqueid
        Point.uniqueid += 1

    @property
    def x(self):
        return self[..., 0]

    @property
    def y(self):
        return self[..., 1]

    @property
    def z(self):
        return self[..., 2]

    def norm(self):
        return np.linalg.norm(self)

    def __repr__(self):
        return 'alg3dpy.Point class'

    def distfrom(self, entity, extend_other=False):
        from .distances import distptpt, distlinept, distplanept
        from .line import Line
        from .plane import Plane
        if (isinstance(entity, list) or isinstance(entity, tuple) or
                isinstance(entity, Point)):
            return distptpt(self, entity)
        elif isinstance(entity, Line):
            return distlinept(entity, self, extend_line=extend_other)
        if isinstance(entity, Plane):
            return distplanept(entity, self)

def aspoint(a):
    from .constants import FLOAT
    if isinstance(a, Point):
        return a
    else:
        return np.asarray(a, dtype=FLOAT).view(Point)




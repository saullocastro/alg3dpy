from __future__ import absolute_import

import numpy as np

from .point import Point
from .distances import distlinept, distplaneline, distlineline
from .angles import angleplaneline, anglelinevec, angle2lines
from .intersections import intersect2lines, intersectplaneline

class Line(np.ndarray):
    """
    Line[0] = pt1
    Line[1] = pt2
    """
    uniqueid = 1
    def __array_finalize(self, obj):
        self.id = Line.uniqueid
        Line.uniqueid += 1

    @property
    def pt1(self):
        return self[0].view(Point)

    @property
    def pt2(self):
        return self[1].view(Point)

    def __repr__(self):
        return 'alg3dpy.Line class'

    def anglewith(self, entity):
        cname = entity.__class__.__name__
        if 'Plane' in cname:
            return angleplaneline(entity, self)
        elif 'Vec' in cname:
            return anglelinevec(self, entity)
        elif 'Line' in cname:
            return angle2lines(self, entity)

    def distfrom(self, entity, extend_me=False, extend_other=False):
        cname = entity.__class__.__name__
        if 'Point' in cname or 'list' in cname or 'tuple' in cname or 'ndarray' in cname:
            return distlinept(self, entity, extend_me)
        elif 'Plane' in cname:
            return distplaneline(self, entity, extend_me)
        elif 'Line' in cname:
            return distlineline(self, entity)

    def intersect(self, entity, extend_me=False, extend_other=False):
        cname = entity.__class__.__name__
        if 'Line' in cname:
            return intersect2lines(self, entity, extend_me, extend_other)
        elif 'Plane' in cname:
            return intersectplaneline(entity, self, extend_me)

    def pt(self, t):
        tmp = np.array([self.pt1[0] + t * (self.pt2[0] - self.pt1[0]),
                        self.pt1[1] + t * (self.pt2[1] - self.pt1[1]),
                        self.pt1[2] + t * (self.pt2[2] - self.pt1[2])])
        return tmp.view(Point)

    def extendto(self, entity, extend_other=False):
        tmp = self.intersect(entity, True, extend_other)
        if tmp is not None:
            check = entity.distfrom(self.pt1) < entity.distfrom(self.pt2)
            self.pt1[check] = tmp[check]
            self.pt2[~check] = tmp[~check]
            return True

        else:
            return False

def asline(a):
    from .constants import FLOAT
    if isinstance(a, Line):
        return a
    else:
        return np.asarray(a, dtype=FLOAT).view(Line)

def ptinline(line, t):
    return asline(line).pt(t)


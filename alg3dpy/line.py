import numpy as np

from point import Point
from distances import distlinept, distplaneline, distlineline
from angles import angleplaneline, anglelinevec, angle2lines
from intersections import intersect2lines, intersectplaneline

def ptinline(line, t):
    #TODO vectorize this
    tmp = np.array([line.pt1[0] + t * (line.pt2[0] - line.pt1[0]),
                    line.pt1[1] + t * (line.pt2[1] - line.pt1[1]),
                    line.pt1[2] + t * (line.pt2[2] - line.pt1[2])])
    return tmp.view(Point)

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
        return self[0]

    @property
    def pt2(self):
        return self[1]

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
            return distplaneline(plane, line, extend_me)
        elif 'Line' in cname:
            return distlineline(self, entity)

    def intersect(self, entity, extend_me=False, extend_other=False):
        cname = entity.__class__.__name__
        if 'Line' in cname:
            return intersect2lines(self, entity, extend_me, extend_other)
        elif 'Plane' in cname:
            return intersectplaneline(plane, self, extend_me)

    def pt(self, t):
        return ptinline(self, t)

    def extendto(self, entity, extend_other=False):
        tmp = self.intersect(entity, True, extend_other)
        if tmp is not None:
            check = entity.distfrom(self.pt1) < entity.distfrom(self.pt2)
            self.pt1[check] = tmp[check]
            self.pt2[~check] = tmp[~check]
            return True

        else:
            return False

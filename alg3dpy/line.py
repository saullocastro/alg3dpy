import numpy as np

from constants import MAXID
from point import Point
from distances import distlinept, distplaneline, distlineline
from angles import angleplaneline, anglelinevec, angle2lines
from intersections import intersect2lines, intersectplaneline

def ptinline(line, t):
    tmp = np.array([line.pt1[0] + t * (line.pt2[0] - line.pt1[0]),
                    line.pt1[1] + t * (line.pt2[1] - line.pt1[1]),
                    line.pt1[2] + t * (line.pt2[2] - line.pt1[2])])
    return tmp.view(Point)

class Line(object):
    """
    Line[0] = pt1
    Line[1] = pt2
    """
    uniqueid = 1
    def __array_finalize(self):
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
        if cname == 'Plane':
            return angleplaneline(entity, self)
        elif cname == 'Vec':
            return anglelinevec(self, entity)
        elif cname == 'Line':
            return angle2lines(self, entity)

    def distfrom(self, entity, extend_me=False, extend_other=False):
        cname = entity.__class__.__name__
        if cname == 'Point' or cname == 'list':
            return distlinept(self, entity, extend_me)
        elif cname == 'Plane':
            return distplaneline(plane, line, extend_me)
        elif cname == 'Line':
            return distlineline(self, entity)

    def intersect(self, entity, extend_me=False, extend_other=False):
        cname = entity.__class__.__name__
        if cname.find('Line') > -1:
            return intersect2lines(self, entity, extend_me, extend_other)
        elif cname.find('Plane') > -1:
            return intersectplaneline(plane, self, extend_me)

    def pt(self, t):
        return ptinline(self, t)

    def extendto(self, entity, extend_other=False):
        tmp = self.intersect(entity, True, extend_other)
        if tmp is not None:
            check = entity.distfrom(self.pt1) < entity.distfrom(self.pt2):
            self.pt1[check] = tmp[check]
            self.pt2[~check] = tmp[~check]
            return True

        else:
            return False

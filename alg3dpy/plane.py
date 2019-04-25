from __future__ import absolute_import

import numpy as np
from numpy.linalg import det


class Plane(object):
    def __init__(self, A=None, B=None, C=None, D=None):
        from .vector import Vec
        from .constants import FLOAT
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.normal = np.array([A, B, C], dtype=FLOAT).view(Vec)

    def __str__(self):
        return 'Plane: A = %2.3f, B = %2.3f, C = %2.3f, D = %2.3f' % \
               (float(self.A), float(self.B), float(self.C), float(self.D))

    def __repr__(self):
        return 'alg3dpy Plane class'

    def anglewith(self, entity):
        from .angles import angle2planes, angleplaneline, angleplanevec
        from .line import Line
        from .plane import Plane
        from .vector import Vec
        if isinstance(entity, Plane):
            return angle2planes(self, entity)
        elif isinstance(entity, Line):
            return angleplaneline(self, entity)
        elif isinstance(entity, Vec):
            return angleplanevec(self, entity)
        else:
            raise NotImplementedError

    def distfrom(self, entity, extend_other=False):
        from .distances import distplanept, distplaneline, distplaneplane
        from .plane import Plane
        from .line import Line
        if isinstance(entity, Line):
            return distplaneline(self, entity, extend_line=extend_other)
        elif isinstance(entity, Plane):
            return distplaneplane(self, entity)
        elif (isinstance(entity, list) or isinstance(entity, tuple) or
                isinstance(entity, np.ndarray)):
            return distplanept(self, entity)
        else:
            raise NotImplementedError


def normplane(plane):
    norm = np.sqrt(plane.A**2 + plane.B**2 + plane.C**2)
    return Plane(plane.A / norm, plane.B / norm, plane.C / norm, plane.D / norm)


def plane1vec1pt(vec1, pt):
    D = (- vec1[0] * pt[0]
         - vec1[1] * pt[1]
         - vec1[2] * pt[2])
    return Plane(vec1[0], vec1[1], vec1[2], D)


def plane3points(pt1, pt2, pt3):
    from .constants import FLOAT
    tmp = np.array([[1., pt1[1], pt1[2]],
                    [1., pt2[1], pt2[2]],
                    [1., pt3[1], pt3[2]]], dtype=FLOAT)
    A = det(tmp)
    tmp = np.array([[pt1[0], 1., pt1[2]],
                    [pt2[0], 1., pt2[2]],
                    [pt3[0], 1., pt3[2]]], dtype=FLOAT)
    B = det(tmp)
    tmp = np.array([[pt1[0], pt1[1], 1.],
                    [pt2[0], pt2[1], 1.],
                    [pt3[0], pt3[1], 1.]], dtype=FLOAT)
    C = det(tmp)
    tmp = np.array([[pt1[0], pt1[1], pt1[2]],
                    [pt2[0], pt2[1], pt2[2]],
                    [pt3[0], pt3[1], pt3[2]]], dtype=FLOAT)
    D = -det(tmp)
    return normplane(Plane(A, B, C, D))


def plane2lines(line1, line2):
    from .vector import ortvec2vecs
    from .line import asline
    line1 = asline(line1)
    line2 = asline(line2)
    ortvec = ortvec2vecs(line1.pt2 - line1.pt1, line2.pt2 - line2.pt1)
    return plane1vec1pt(ortvec, line1.pt1)

from __future__ import absolute_import

import numpy as np


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
        if entity.__class__.__name__ == 'Plane':
            return angle2planes(self, entity)
        if entity.__class__.__name__ == 'Line':
            return angleplaneline(self, entity)
        if entity.__class__.__name__ == 'Vec':
            return angleplanevec(self, entity)

    def distfrom(self, entity):
        from .distances import distplanept, distplaneline, distplaneplane
        if entity.__class__.__name__ == 'Point':
            return distplanept(self, entity)
        if entity.__class__.__name__ == 'Line':
            return distplaneline(self, entity)
        if entity.__class__.__name__ == 'Plane':
            return distplaneplane(self, entity)


def plane1vec1pt(vec1, pt):
    D = (- vec1[0] * pt[0]
         - vec1[1] * pt[1]
         - vec1[2] * pt[2])
    return Plane(vec1[0], vec1[1], vec1[2], D)


def plane3points(pt1, pt2, pt3):
    from .constants import FLOAT
    from .arrays import arraydet

    tmp = np.array([[1., pt1[1], pt1[2]],
                    [1., pt2[1], pt2[2]],
                    [1., pt3[1], pt3[2]]], dtype=FLOAT)
    A = arraydet(tmp)
    tmp = np.array([[pt1[0], 1., pt1[2]],
                    [pt2[0], 1., pt2[2]],
                    [pt3[0], 1., pt3[2]]], dtype=FLOAT)
    B = arraydet(tmp)
    tmp = np.array([[pt1[0], pt1[1], 1.],
                    [pt2[0], pt2[1], 1.],
                    [pt3[0], pt3[1], 1.]], dtype=FLOAT)
    C = arraydet(tmp)
    tmp = np.array([[pt1[0], pt1[1], pt1[2]],
                    [pt2[0], pt2[1], pt2[2]],
                    [pt3[0], pt3[1], pt3[2]]], dtype=FLOAT)
    D = -arraydet(tmp)
    return normplane(A, B, C, D)


def plane2lines(line1, line2):
    from .vector import ortvec2vecs
    ortvec = ortvec2vecs(line1.pt2 - line1.pt1, line2.pt2 - line2.pt1)
    return plane1vec1pt(ortvec, line1.pt1)


def normplane( plane ):
    norm = np.sqrt(plane.A**2 + plane.B**2 + plane.C**2)
    return Plane(plane.A / norm, plane.B / norm, plane.C / norm, plane.D / norm)

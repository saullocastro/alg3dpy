from __future__ import absolute_import

import numpy as np

from .plane import normplane
from .angles import angle2lines
from .intersections import intersectplaneline

def distplanept(plane, pt):
    from .point import aspoint
    pt = aspoint(pt)
    return (plane.A * pt[0] +
            plane.B * pt[1] +
            plane.C * pt[2] + plane.D) / plane.normal.mod()

def distplaneplane(plane1, plane2):
    return np.abs(normplane(plane1).D - normplane(plane2).D)

def distplaneline(plane, line, extend_line=False):
    from .line import asline
    line = asline(line)
    if intersectplaneline(plane, line, extend_line) is False:
        d1 = distplanept(plane, line.pt1)
        d2 = distplanept(plane, line.pt2)
        return np.array((d1, d2)).min(axis=0)
    else:
        return 0

def distptpt(pt1, pt2):
    from .point import aspoint
    pt1 = aspoint(pt1)
    pt2 = aspoint(pt2)
    return np.sqrt(((pt2 - pt1)**2).sum(axis=-1))

def distlinept(line, pt, extend_line=False):
    from .line import asline
    from .point import aspoint
    line = asline(line)
    pt = aspoint(pt)
    x1 = line.pt1[0]
    y1 = line.pt1[1]
    z1 = line.pt1[2]
    x2 = line.pt2[0]
    y2 = line.pt2[1]
    z2 = line.pt2[2]
    x3 = pt[0]
    y3 = pt[1]
    z3 = pt[2]
    den = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    t = ((x1**2 + x2 * x3 - x1 * x3 - x1 * x2 +
          y1**2 + y2 * y3 - y1 * y3 - y1 * y2 +
          z1**2 + z2 * z3 - z1 * z3 - z1 * z2)/den)
    if not extend_line:
        if t > 1: t = 1
        if t < 0: t = 0
    return distptpt(line.pt(t), pt)

def distlineline(line1, line2, extend_line1=False, extend_line2=False):
    from .line import asline
    line1 = asline(line1)
    line2 = asline(line2)
    x1a = line1.pt1[0]
    y1a = line1.pt1[1]
    z1a = line1.pt1[2]
    x1b = line1.pt2[0]
    y1b = line1.pt2[1]
    z1b = line1.pt2[2]
    x2a = line2.pt1[0]
    y2a = line2.pt1[1]
    z2a = line2.pt1[2]
    x2b = line2.pt2[0]
    y2b = line2.pt2[1]
    z2b = line2.pt2[2]
    C1 = ((x2b - x2a) * (x1b - x1a) +
          (y2b - y2a) * (y1b - y1a) +
          (z2b - z2a) * (z1b - z1a))
    C2 = (x1b - x1a)**2 + (y1b - y1a)**2 + (z1b - z1a)**2
    C3 = ((x1a * (-x1a + x2a + x1b) - x1b * x2a) +
          (y1a * (-y1a + y2a + y1b) - y1b * y2a) +
          (z1a * (-z1a + z2a + z1b) - z1b * z2a))
    C4 = (x2b - x2a)**2 + (y2b - y2a)**2 + (z2b - z2a)**2
    C5 = ((x2a * (x2a - x1a - x2b) + x1a * x2b) +
          (y2a * (y2a - y1a - y2b) + y1a * y2b) +
          (z2a * (z2a - z1a - z2b) + z1a * z2b))
    if angle2lines(line1, line2) < 0.01:
        return distlinept(line1, line2.pt1, extend_line1)
    else:
        t = (C1 * C5 - C4 * C3) / (C2 * C4 - C1**2)
        u = (C2 * C5 - C1 * C3) / (C2 * C4 - C1**2)
        if extend_line1 == False:
            if t > 1: t = 1
            if t < 0: t = 0
        if extend_line2 == False:
            if u > 1: u = 1
            if u < 0: u = 0
        return distptpt(line1.pt(t), line2.pt(u))

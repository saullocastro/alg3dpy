from __future__ import absolute_import

import numpy as np


def intersectplaneline(plane, line, extend_line=False):
    from .constants import TOL
    from .line import asline, Line
    from .plane import Plane
    line = asline(line)
    if not isinstance(plane, Plane):
        raise ValueError('Input is not a valid plane!')
    if np.dot(plane.normal, line.pt2 - line.pt1) < TOL:
        return None
    x1 = line.pt1.x
    y1 = line.pt1.y
    z1 = line.pt1.z
    x2 = line.pt2.x
    y2 = line.pt2.y
    z2 = line.pt2.z
    t = ((plane.A * x1 + plane.B * y1 + plane.C * z1 + plane.D) /
         (plane.A * (x1 - x2) + plane.B * (y1 - y2) + plane.C * (z1 - z2)))
    if (t > 1 or t < 0) and not extend_line:
        print('Intersection solvable only with extend_line=True, returning None')
        return None
    return line.pt(t)

def intersect2lines(line1, line2, extend_line1=False, extend_line2=False):
    #http://paulbourke.net/geometry/lineline3d/
    from .constants import TOL, ZER
    from .line import asline
    line1 = asline(line1)
    line2 = asline(line2)
    v13 = line2.pt1 - line1.pt1
    v43 = line2.pt1 - line2.pt2
    v21 = line1.pt1 - line1.pt2
    d1343 = v13.x * v43.x + v13.y * v43.y + v13.z * v43.z
    d4321 = v43.x * v21.x + v43.y * v21.y + v43.z * v21.z
    d1321 = v13.x * v21.x + v13.y * v21.y + v13.z * v21.z
    d4343 = v43.x * v43.x + v43.y * v43.y + v43.z * v43.z
    d2121 = v21.x * v21.x + v21.y * v21.y + v21.z * v21.z
    denom = d2121 * d4343 - d4321 * d4321
    if abs(denom) <= ZER:
        return None
    else:
        numer = d1343 * d4321 - d1321 * d4343
        s = numer/denom
        t = (d1343 + d4321*s)/d4343
        if extend_line1 == False:
            s = min(s, 1)
            s = max(s, 0)
        if extend_line2 == False:
            t = min(t, 1)
            t = max(t, 0)
        ptline1 = line1.pt(s)
        ptline2 = line2.pt(t)
        disttest1 = ptline1.distfrom(ptline2)
        if disttest1 > TOL:
            return None
        else:
            return (ptline1 + ptline2) / 2.

from constants import TOL, ZER
import sys
import numpy as np
#
# INTERSECTION OPERATIONS
#
def intersectplaneline(plane, line, extend_line = False):
    if plane.__class__.__name__ <> 'Plane':
        print 'Input is not a valid plane!'
        sys.exit()
    if line.__class__.__name__ <> 'Line':
        print 'Input is not a valid line!'
        sys.exit()
    if np.dot( plane.normal, Vec( line.array ) ) < TOL:
        return False
        sys.exit()
    x1 = line.pt1.x1
    y1 = line.pt1.x2
    z1 = line.pt1.x3
    x2 = line.pt2.x1
    y2 = line.pt2.x2
    z2 = line.pt2.x3
    t = (plane.A * x1 + plane.B * y1 + plane.C * z1 + plane.D) / \
        (plane.A * (x1 - x2) + plane.B * (y1 - y2) + plane.C * (z1 - z2))
    if extend_line == False:
        if t > 1 or t < 0:
            #uncomment after adding a caller identifier.... then allowing message only for a None caller
            #print '''Intersection found beyond line limits. Soluble for 'extend=True'.'''
            return False
            sys.exit()
    return line.pt(t)

def intersect2lines(line1, line2, extend_line1=False, extend_line2=False):
    #http://paulbourke.net/geometry/lineline3d/
    v13 = line2.pt1 - line1.pt1
    v43 = line2.pt1 - line2.pt2
    v21 = line1.pt1 - line1.pt2
    d1343 = v13.i * v43.i + v13.j * v43.j + v13.k * v43.k
    d4321 = v43.i * v21.i + v43.j * v21.j + v43.k * v21.k
    d1321 = v13.i * v21.i + v13.j * v21.j + v13.k * v21.k
    d4343 = v43.i * v43.i + v43.j * v43.j + v43.k * v43.k
    d2121 = v21.i * v21.i + v21.j * v21.j + v21.k * v21.k
    denom = d2121 * d4343 - d4321 * d4321
    if abs(denom) < ZER:
        return None
    else:
        numer = d1343 * d4321 - d1321 * d4343
        s = numer / denom
        t = (d1343 + d4321 * s) / d4343
        if extend_line1 == False:
            if s < 0: s = 0
            if s > 1: s = 1
        if extend_line2 == False:
            if t < 0: t = 0
            if t > 1: t = 1
        ptline1 = line1.pt(s)
        ptline2 = line2.pt(t)
        disttest1 = ptline1.distfrom(ptline2)
        if disttest1 > TOL:
            return None
        else:
            ans = ptline1.__add__(ptline2, vec=False) * 0.5
            return ans

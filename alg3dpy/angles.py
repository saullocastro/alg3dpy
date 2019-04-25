from __future__ import absolute_import

import numpy as np

from .vector import asvector


def cos2vecs(vec1, vec2):
    vec1 = asvector(vec1)
    vec2 = asvector(vec2)
    return np.dot(vec1, vec2) / (vec1.mod() * vec2.mod())


def sin2vecs(vec1, vec2):
    vec1 = asvector(vec1)
    vec2 = asvector(vec2)
    c = cos2vecs(vec1, vec2)
    return np.sqrt(1 - c**2)


def sinplanevec(plane, vec):
    from .plane import Plane
    assert isinstance(plane, Plane)
    vec = asvector(vec)
    c = cos2vecs(plane.normal, vec)
    return c


def cosplanevec(plane, vec):
    from .plane import Plane
    assert isinstance(plane, Plane)
    vec = asvector(vec)
    s = sinplanevec(plane, vec)
    return np.sqrt(1 - s**2)


def angle2vecs(vec1, vec2):
    return np.arccos(cos2vecs(vec1, vec2))


def angle2planes(plane1, plane2):
    from .plane import Plane
    assert isinstance(plane1, Plane)
    assert isinstance(plane2, Plane)
    return angle2vecs(plane1.normal, plane2.normal)


def angleplanevec(plane, vec):
    from .plane import Plane
    assert isinstance(plane, Plane)
    vec = asvector(vec)
    return (np.pi/2 - angle2vecs(plane.normal, vec))


def angleplaneline(plane, line):
    from .line import asline
    from .plane import Plane
    assert isinstance(plane, Plane)
    line = asline(line)
    return (np.pi/2 - angle2vecs(plane.normal, line.pt2 - line.pt1))


def anglelinevec(line, vec):
    from .line import asline
    vec = asvector(vec)
    line = asline(line)
    return angle2vecs(line.pt2 - line.pt1, vec)


def angle2lines(line1, line2):
    from .line import asline
    line1 = asline(line1)
    line2 = asline(line2)
    return angle2vecs(line1.pt2 - line1.pt1, line2.pt2 - line2.pt1)

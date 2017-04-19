from __future__ import absolute_import

import numpy as np

from .point import aspoint


def area_tria(p1, p2, p3):
    p1 = aspoint(p1)
    p2 = aspoint(p2)
    p3 = aspoint(p3)
    a = p1.distfrom(p2)
    b = p1.distfrom(p3)
    c = p2.distfrom(p3)
    p = (a + b + c)/2.
    area = np.sqrt(p*(p-a)*(p-b)*(p-c))
    print('DEBUG area', area)
    return area

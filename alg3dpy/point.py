import numpy as np

from constants import FLOAT, MAXID
from distances import distptpt, distlinept, distplanept

class Point(np.ndarray):
    uniqueid = 1

    def __array_finalize__(self):
        self.id = Point.uniqueid
        Point.uniqueid += 1

    @property
    def x(self):
        return self[..., 0]

    @property
    def y(self):
        return self[..., 1]

    @property
    def z(self):
        return self[..., 2]

    def norm(self):
        return np.linalg.norm(self)

    def __str__( self ):
        return str( self)
        #return 'Point ID %d: x1 = %2.3f, x2 = %2.3f, x3 = %2.3f'\
        #        % (self.id, self[0], self[1], self[2])

    def __repr__( self ):
        return 'alg3dpy.Point class'

    def distfrom(self, entity):
        cname = entity.__class__.__name__
        if cname == 'Point' or cname == 'Grid':
            return distptpt(self, entity)
        if cname == 'Line':
            return distlinept(entity, self)
        if cname == 'Plane':
            return distplanept(entity, self)


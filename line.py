import random as rdm
import numpy as np
from point import Point
from constants import MAXID
def ptinline(line, t):
    tmp = np.array(\
        [ line.pt1.array[0] + t * (line.pt2.array[0] - line.pt1.array[0]),\
          line.pt1.array[1] + t * (line.pt2.array[1] - line.pt1.array[1]),\
          line.pt1.array[2] + t * (line.pt2.array[2] - line.pt1.array[2]) ])
    return Point(tmp)

class Line(object):

    def __init__( self, pt1, pt2,id=None):
        if id == None:
            self.id = int( MAXID*rdm.random() )
        cname1 = pt1.__class__.__name__
        self.pt1 = Point(pt1)
        self.pt2 = Point(pt2)
        if self.pt1.array <> None and self.pt2.array <> None:
            self.array = self.pt2.array - self.pt1.array

    def __str__(self):
        return 'Line ID %d: pt1 = %2.3f,%2.3f,%2.3f ; pt2 = %2.3f,%2.3f,%2.3f'\
               % (self.id,\
                  self.pt1.array[0], self.pt1.array[1], self.pt1.array[2], \
                  self.pt2.array[0], self.pt2.array[1], self.pt2.array[2])
    
    def __repr__(self):
        return 'alg3dpy Line class'
        
    def __getitem__(self, item):
        if   item == 0:
            return self.pt1
        elif item > 0:
            return self.pt2

    def anglewith(self, entity):
        if   entity.__class__.__name__ == 'Plane':
            from angles import angleplaneline
            return angleplaneline(entity, self)
        elif entity.__class__.__name__ == 'Vec':
            from angles import anglelinevec
            return anglelinevec(self, entity)
        elif entity.__class__.__name__ == 'Line':
            from angles import angle2lines
            return angle2lines(self, entity)
           
    def distfrom(self, entity, extend_me=False, extend_other=False):
        if   entity.__class__.__name__ == 'Point' or \
             entity.__class__.__name__ == 'list':
            from distances import distlinept
            return distlinept(self, entity, extend_me)
        elif entity.__class__.__name__ == 'Plane':
            from distances import distplaneline
            return distplaneline(plane, line, extend_me)
        elif entity.__class__.__name__ == 'Line':
            from distances import distlineline
            return distlineline(self, entity)

    def intersect(self, entity, extend_me=False, extend_other=False):
        if   entity.__class__.__name__.find('Line') > -1:
            from intersections import intersect2lines
            return intersect2lines(self, entity, extend_me, extend_other)
        elif entity.__class__.__name__.find('Plane') > -1:
            from intersections import intersectplaneline
            return intersectplaneline(plane, self, extend_me)

    def pt(self, t):
        return ptinline(self, t)

    def extendto(self, entity, extend_other = False):
        tmp = self.intersect(entity, True, extend_other)
        if tmp <> None:
            if entity.distfrom( self.pt1 ) < entity.distfrom( self.pt2 ):
                self.pt1 = tmp
            else:
                self.pt2 = tmp
            return True
        else:
            return False

import random as rdm
import numpy as np
from vector import Vec
from constants import FLOAT, MAXID
from distances import distptpt, distlinept, distplanept
class Point(object):
    def __init__( self, input = None, id = None ):
        self.array = None
        self.id    = None
        #
        if id == None:
            self.id = int( MAXID*rdm.random() )
        if input.__class__.__name__.find( 'Point' ) > -1:
            self = input
            return
        elif input.__class__.__name__.find( 'Vec' ) > -1:
            self.array = input.array
            self.id = input.id
            return
        else:
            from checkarg import checkarray
            self.array = checkarray( input )
    
    def __add__( self, entity, vec=True ):
        if vec == False:
            return Point( self.array + entity.array )
        else:
            return Vec( self.array + entity.array )

    def __sub__( self, entity, vec=True ):
        if vec == False:
            return Point( self.array - entity.array )
        else:    
            return Vec( self.array - entity.array )

    def __div__( self, number ):
        return Point( self.array / float(number) )

    def __mul__( self, number ):
        return Point( self.array * float(number) )

    def __getitem__( self, item ):
        return self.array[ item ]
    
    def __setitem__( self, item, value ):
        self.array[ item ] = value
    
    def mod( self ):
        return np.sqrt( self.array[0]**2 \
                      + self.array[1]**2 \
                      + self.array[2]**2 )

    def __str__( self ):
        return str( self.array )
        #return 'Point ID %d: x1 = %2.3f, x2 = %2.3f, x3 = %2.3f'\
        #        % (self.id, self.array[0], self.array[1], self.array[2])

    def __repr__( self ):
        return 'alg3dpy Point class'
    
    def distfrom( self, entity ):
        cname = entity.__class__.__name__
        if cname == 'Point' or cname == 'Grid' :
            return distptpt( self, entity )
        if cname == 'Line':
            return distlinept( entity, self )
        if cname == 'Plane':
            return distplanept( entity, self)
    

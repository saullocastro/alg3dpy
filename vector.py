from alg3dpy.constants import MAXID
import numpy as np
import random as rdm
class Vec(object):

    def __init__( self, numpy_array = np.zeros([3]) ):
        from checkarg import checkarray
        self.id = int( MAXID*rdm.random() )
        self.array = checkarray( numpy_array )

    def __add__( self, entity ):
        return Vec( self.array + entity.array )

    def __sub__( self, entity ):
        return Vec( self.array - entity.array )

    def __mul__( self, vec2 ):
        return Vec( self.array * vec2.array )

    def __pow__( self, vec2 ):
        return Vec( np.cross( self.array, vec2.array ) )
    
    def __getitem__( self, item ):
        return self.array[ item ]
    
    def __setitem__( self, item, value ):
        self.array[ item ] = value
    
    def dot( self, vec2 ):
        return np.dot( self.array, vec2.array )

    def norm(self):
        self.array /= np.linalg.norm( self.array )

        return self

    def cross(self, vec2 ):
        return Vec( np.cross( self.array, vec2.array ) ).norm()


    def mod( self ):
        return np.linalg.norm( self.array )

    def __str__( self ):
        return 'Vector ID %d: %2.3f i + %2.3f j + %2.3f k'\
               % ( self.id, self.array[0], self.array[1], self.array[2] )

    def __repr__( self ):
        return 'alg3dpy Vector class'
            
    def __getattr__( self, attr ):
        if attr == 'i':
            return self[0]
        elif attr == 'j':
            return self[1]
        elif attr == 'k':
            return self[2]
        else:
            return getattr( self, attr )

    def anglewith( self, entity ):
        if entity.__class__.__name__ == 'Plane':
            return angleplanevec( entity, self )
        if entity.__class__.__name__ == 'Vec':
            return angle2vecs( self, entity )
        if entity.__class__.__name__ == 'Line':
            return anglelinevec( entity, self )

    def cosines_GLOBAL( self ):
        cosbeta = cosplanevec( XY, self )
        cosgama = cosplanevec( XZ, self )
        return [ cosbeta, cosgama ]


#
def ortvec3points( pt1, pt2, pt3 ):
    vec1 = pt2 - pt1
    vec2 = pt3 - pt1
    return ortvec2vecs( vec1, vec2 )

#Weisstein, Eric W. "Normalized Vector." From MathWorld--A Wolfram Web Resource.
#   http://mathworld.wolfram.com/NormalizedVector.html 
#Weisstein, Eric W. "Norm." From MathWorld--A Wolfram Web Resource. 
#   http://mathworld.wolfram.com/Norm.html 

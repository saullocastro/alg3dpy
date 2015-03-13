from constants import FLOAT
from vector import Vec
import numpy as np
#
# ANGLE OPERATIONS
#
def cos2vecs(vec1, vec2):
    return ( np.dot( vec1, vec2 ) / vec1.mod() * vec2.mod() )
    
def sin2vecs(vec1, vec2):
    cos = cos2vecs(vec1, vec2)
    return np.sqrt(1 - cos**2)

def sinplanevec(plane, vec):
    cos = cos2vecs(plane.normal, vec)
    # if alpha + beta = PI/2: cos(alpha) = sin(beta) 
    return cos 

def cosplanevec(plane, vec):
    sin = sinplanevec(plane, vec) 
    # if alpha + beta = PI/2: cos(alpha) = sin(beta) 
    return np.sqrt(1 - sin**2)

def angle2vecs(vec1, vec2):
    return np.rad2deg( np.arccos( cos2vecs(vec1, vec2) ))
    
def angle2planes(plane1,plane2):
    return angle2vecs( plane1.normal, plane2.normal)

def angleplanevec(plane,vec):
    return (90 - angle2vecs( plane.normal, vec ))

def angleplaneline(plane,line):
    return (90 - angle2vecs( plane.normal, Vec( line.array ) ))

def anglelinevec (line,vec):
    return angle2vecs( Vec( line.array ) ,vec )

def angle2lines(line1,line2):
    return angle2vecs( Vec( line1.array), Vec( line2.array ) )

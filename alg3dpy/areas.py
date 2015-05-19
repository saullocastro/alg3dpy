import numpy as np
def area_tria(p1, p2, p3):
     a = p1.distfrom(p2)
     b = p1.distfrom(p3)
     c = p2.distfrom(p3)
     p = (a + b + c)/2.
     return np.sqrt( p*(p-a)*(p-b)*(p-c) )

import numpy as np
MAXID = 99999999
FLOAT = 'float64' # 'float32' 'float128'
INT16 = 'int16'   # 2**16 =           65,536 unique values
INT32 = 'int32'   # 2**32 =    4,294,967,296 unique values
INT64 = 'int64'   # 2**64 = 1.844674407 * 10**19 unique values
INT   = INT32       # default
ONE   = 1.
TOL   = 1e-6
ZER   = 0.
from point import Point
O = Point( np.array((0,0,0), dtype=FLOAT) )
from vector import Vec
X = Vec( np.array((1,0,0), dtype=FLOAT) )
Y = Vec( np.array((0,1,0), dtype=FLOAT) )
Z = Vec( np.array((0,0,1), dtype=FLOAT) )
from plane import plane1vec1pt
PLANEXY = plane1vec1pt(Z, O)
PLANEXZ = plane1vec1pt(Y, O)
PLANEYZ = plane1vec1pt(X, O)


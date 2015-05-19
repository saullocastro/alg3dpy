from constants import ONE,FLOAT
import numpy as np
def multilinear( yvar, *args ):
    numvar = len(args)
    N = len(yvar)
    x = np.zeros(  (N, numvar + 1) ,dtype=FLOAT)
    y = np.array( yvar )
    for i in range( N ):
        for j in range( numvar ):
            x[i][j] = args[j][i] 
        x[i][-1] = ONE
    xt = x.transpose()    
    b = np.dot( xt, y )
    a = np.dot( xt, x )
    c = np.linalg.solve( a, b )
    return c

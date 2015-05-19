import numpy as np
from constants import FLOAT
def checkarray( numpy_array ):
    cname = numpy_array.__class__.__name__
    size = len(numpy_array)
    if size > 3:
        print 'Invalid array size!'
        raise
    if size == 2:
        numpy_array = list(numpy_array)
        numpy_array.append( 0. )
    if cname.find( 'array' ) == -1:
        if cname == 'list'\
        or cname == 'tuple':
            numpy_array = np.array( numpy_array, dtype = FLOAT )
        elif cname.find( 'Vec' ) > -1:
            numpy_array = numpy_array.array
        else:
            print 'Invalid input: must be tuple, list or ndarray!'
            raise
    else:
        if numpy_array.dtype.name <> FLOAT:
            print 'Array must be of dtype = %s' % FLOAT
            print '\t OR modify the FLOAT constant in constants.py'
            print '\t the original dtype = %s had been changed to %s'\
                  % (numpy_array.dtype.name, FLOAT)
            numpy_array = np.array( numpy_array, dtype = FLOAT )      
    return numpy_array

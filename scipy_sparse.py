def in_sparse(m, r1, r2, c1, c2):
    '''m must a coo matrix
    returns an inner matrix of m which is delimited by
    rows r1 and r2 and by
    columns c1 and c2
    '''
    import scipy
    import scipy.sparse as ss
    indices = []
    new_d = []
    new_r = []
    new_c = []
    for d, r, c in zip(m.data, m.row, m.col):
        if r1 <= r and r <= r2 and c1 <= c and c <= c2:
            new_d.append(d)
            new_r.append(r-r1)
            new_c.append(c-c1)
    new_d = scipy.array(new_d, dtype = 'float64')        
    new_r = scipy.array(new_r, dtype = 'int8')
    new_c = scipy.array(new_c, dtype = 'int8')
    dim1 = r2 - r1 + 1
    dim2 = c2 - c1 + 1
    return ss.coo_matrix( (new_d, (new_r,new_c)), shape=(dim1,dim2))

def zero_index (m, list_of_index):
    '''m must be a coo matrix
       changes to 0. all elements into m with the row or column index
       equal any indexes contained in list_of_index
    '''
    mout = m.copy()
    if len(list_of_index) >= len(mout.data):
        for ind in list_of_index:
            for i in xrange(len(mout.data)):
                if (mout.row[i] == ind or mout.col[i] == ind):
                    mout.data[i] = 0.
    else:
        for i in xrange(len(mout.data)):
            for ind in list_of_index:
                if (mout.row[i] == ind or mout.col[i] == ind):
                    mout.data[i] = 0.
    return mout
def diag_ones (m):
    '''m cannot be of coo type
       changes all diagonals with 0. value to 1.
    '''
    diag = m.diagonal()
    for i in xrange(len(diag)):
        if diag[i] < 1e-8:
            diag[i] = 1.
    m.setdiag(diag)       
    return m
            
def del_index (m, list_of_index):
    if m.__class__.__name__.find('array') > -1:
        dim = len(m) - len(list_of_index)
        mout = scipy.zeros(shape=dim, dtype = m.dtype)
        j = -1
        for i in xrange(len(m)):
            if not i in list_of_index:
                j += 1
                mout[j] = m[i]
        return mout       

    ''' m must be a coo matrix
        a new matrix without the rows and columns given in
        list_of_index will be returned
    '''
    import scipy
    import scipy.sparse as ss
    #finding number of rows/cols to exclude
    countdel = 0
    for i in xrange(len(m.data)):
        for ind in list_of_index:
            if m.row[i] == ind or m.col[i] == ind:
                countdel += 1
                break
    nnz = m.nnz - countdel            
    data = scipy.zeros(nnz, dtype=m.data.dtype)
    row  = scipy.zeros(nnz, dtype=scipy.intc)
    col  = scipy.zeros(nnz, dtype=scipy.intc)
    #copying new values
    j = 0 
    indlast = -1
    add = False
    for i in xrange(len(m.data)):
        offsetr = 0
        offsetc = 0
        for k in xrange(len(list_of_index)):
            ind = list_of_index[k]
            if m.row[i] == ind or m.col[i] == ind:
                add = False
                break
            else:
                add = True
            offcheckr = m.row[i]
            offcheckc = m.col[i]
            if offcheckr > ind and offsetr < k + 1:
                offsetr = k + 1
            if offcheckc > ind and offsetc < k + 1:
                offsetc = k + 1
        if add:        
            data[j] = m.data[i]
            row[j] = m.row[i] - offsetr
            col[j] = m.col[i] - offsetc
            j += 1

    dim = m.shape[0] - len(list_of_index)            

    return ss.coo_matrix( (data, (row, col)), shape=(dim,dim))
        

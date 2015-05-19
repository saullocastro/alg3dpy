import numpy as np
class LinearSystem:
    '''
        Defines a class for the linear system Ax = b
    '''
    def __init__(self, A, b):
        self.A = A
        self.b = b
    def solve_conjugate_grad(self, maxiter=1000, tol=1.e-6):
        x = []
        r = []
        rt = []
        p = []
        pt = []
        x.append(zeros(len(self.A), 1))
        x[0] = arraykmult(0.0, x[0])
        r.append(arraysub(self.b, arraymult(self.A,x[0])))
        rt.append(arraytranspose(r[0]))
        p.append(r[0])
        pt.append(rt[0])
        for i in xrange(maxiter):
            try:
                alpha = arraymult(rt[i], r[i])[0][0] / float(arraymult(arraymult(pt[i], self.A), p[i])[0][0])
            except:
                self.x = x[-1]
                return x[-1]
            x.append(arraysum(x[i], arraykmult(alpha, p[i])))
            r.append(arraysub(r[i], arraymult(arraykmult(alpha, self.A), p[i])))
            if r[i + 1] <= tol:
                break
            rt.append(arraytranspose(r[i + 1]))
            num = arraymult(rt[i + 1], r[i + 1])
            den = arraymult(rt[i], r[i])
            beta = num[0][0] / float(den[0][0])
            p.append(arraysum(r[i + 1], arraykmult(beta, p[i])))
            pt.append(arraytranspose(p[i + 1]))
        self.x = x[-1]
        return x[-1]

#
def arraydet(numpy_array):
    a11 = numpy_array[0][0]
    a21 = numpy_array[1][0]
    a31 = numpy_array[2][0]
    a12 = numpy_array[0][1]
    a22 = numpy_array[1][1]
    a32 = numpy_array[2][1]
    a13 = numpy_array[0][2]
    a23 = numpy_array[1][2]
    a33 = numpy_array[2][2]
    return (a11*a22*a33 + a12*a23*a31 + a13*a21*a32 \
           -a13*a22*a31 - a11*a23*a32 - a12*a21*a33)

def arraydet44(numpy_array):
    a11 = numpy_array[0][0]
    a21 = numpy_array[1][0]
    a31 = numpy_array[2][0]
    a41 = numpy_array[3][0]
    a12 = numpy_array[0][1]
    a22 = numpy_array[1][1]
    a32 = numpy_array[2][1]
    a42 = numpy_array[3][1]
    a13 = numpy_array[0][2]
    a23 = numpy_array[1][2]
    a33 = numpy_array[2][2]
    a43 = numpy_array[3][2]
    a14 = numpy_array[0][3]
    a24 = numpy_array[1][3]
    a34 = numpy_array[2][3]
    a44 = numpy_array[3][3]
    return a11 * det(a22,a23,a24,a32,a33,a34,a42,a43,a44) - \
           a12 * det(a21,a23,a24,a31,a33,a34,a41,a43,a44) - \
           a13 * det(a21,a22,a24,a31,a32,a34,a41,a42,a44) + \
           a14 * det(a21,a22,a23,a31,a32,a33,a41,a42,a43)

def arrayconact_v(m1, m2):
    res = m1 + m2
    return res

def delete_rows(m, list_of_rows):
    answ = []
    for row_num in xrange(len(m)):
        if not (row_num) in list_of_rows:
            answ.append(m[row_num])
    return answ

def delete_cols(m, list_of_cols):
    answ = []
    for row_num in xrange(len(m)):
        newi = []
        for col_num in xrange(len(m[row_num])):
            if not (col_num) in list_of_cols:
                newi.append(m[row_num][col_num])
        answ.append(newi)
    return answ

def delete_index(m, list_of_index):
    answ = []
    for row_num in xrange(len(m)):
        if not (row_num) in list_of_index:
            newi = []
            for col_num in xrange(len(m[row_num])):
                if not (col_num) in list_of_index:
                    newi.append(m[row_num][col_num])
            answ.append(newi)
    return answ


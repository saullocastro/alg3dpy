from __future__ import absolute_import

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
    return (a11*a22*a33 + a12*a23*a31 + a13*a21*a32
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
    return (a11 * arraydet(a22,a23,a24,a32,a33,a34,a42,a43,a44)
            - a12 * arraydet(a21,a23,a24,a31,a33,a34,a41,a43,a44)
            - a13 * arraydet(a21,a22,a24,a31,a32,a34,a41,a42,a44)
            + a14 * arraydet(a21,a22,a23,a31,a32,a33,a41,a42,a43))

def arrayconact_v(m1, m2):
    res = m1 + m2
    return res

def delete_rows(m, list_of_rows):
    answ = []
    for row_num in range(len(m)):
        if not (row_num) in list_of_rows:
            answ.append(m[row_num])
    return answ

def delete_cols(m, list_of_cols):
    answ = []
    for row_num in range(len(m)):
        newi = []
        for col_num in range(len(m[row_num])):
            if not (col_num) in list_of_cols:
                newi.append(m[row_num][col_num])
        answ.append(newi)
    return answ

def delete_index(m, list_of_index):
    answ = []
    for row_num in range(len(m)):
        if not (row_num) in list_of_index:
            newi = []
            for col_num in range(len(m[row_num])):
                if not (col_num) in list_of_index:
                    newi.append(m[row_num][col_num])
            answ.append(newi)
    return answ


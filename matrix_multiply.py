# ------------------------------------------------------------------------
# This module supports matrix multiplication by Strassen's algorithm
# the ordinary multiplication method
#
# Author: Shuting Chen
# Date Created: 09/22/2022
# Date Last Modified: 09/25/2022
# ------------------------------------------------------------------------


def divide_matrix(m, midpoint):
    """
        Divide a matrix into four 1/2n*1/2n matrices.

            m: 2D matrices wait to be partitioned
            Return:
                m11, m12, m21, m22: the four 1/2n*1/2n matrices
    """
    m11 = []
    m12 = []
    m21 = []
    m22 = []
    ct = 0
    for i in m:
        if ct < midpoint:
            m11.append(i[0:midpoint])
            m12.append(i[midpoint:])
        else:
            m21.append(i[0:midpoint])
            m22.append(i[midpoint:])
        ct += 1

    return m11, m12, m21, m22


def matrix_calculation(m1, m2, operator):
    """
            Assemble four 1/2n*1/2n matrices back to a whole.

            m1, m2: 2D matrices wait for calculation
            Return:
                res: the result matrix
    """
    res = []
    if operator == "-":
        for i in range(0, len(m1)):
            res.append([m1[i][j] - m2[i][j] for j in range(0, len(m1))])
    if operator == "+":
        for i in range(0, len(m1)):
            res.append([m1[i][j] + m2[i][j] for j in range(0, len(m1))])
    return res


def matrix_assemble(c1, c2, c3, c4):
    """
            Assemble four 1/2n*1/2n matrices back to a whole.

            c1, c2, c3, c4: 2D sub-matrices
            Return:
                C: the final matrix
    """
    res = []
    for i in range(0, len(c1)):
        res.append(c1[i] + c2[i])
    for i in range(0, len(c3)):
        res.append(c3[i] + c4[i])
    return res




def strassen_multiply(A, B):
    """
        Implementing Strassen's algorithm to do matrix multiplication

        A: One of the input matrices
        B: Another input matrix
        Return:
            C: the product matrix C multiplied from A and B
            ct: counter for multiplication
    """

    # initiate counter for analyzing computational cost
    ct = 0

    # Base condition
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]], 0
    else:
        # divide the input n*n matrices into 1/2n*1/2n submatrices
        midpoint = n // 2

        A11, A12, A21, A22 = divide_matrix(A, midpoint)
        B11, B12, B21, B22 = divide_matrix(B, midpoint)

        # compute 7 intermediate matrices p1, p2...p7
        P1, ct_temp = strassen_multiply(A11, matrix_calculation(B12, B22, "-"))
        ct += ct_temp
        P2, ct_temp = strassen_multiply(matrix_calculation(A11, A12, "+"), B22)
        ct += ct_temp
        P3, ct_temp = strassen_multiply(matrix_calculation(A21, A22, "+"), B11)
        ct += ct_temp
        P4, ct_temp = strassen_multiply(A22, matrix_calculation(B21, B11, "-"))
        ct += ct_temp
        P5, ct_temp = strassen_multiply(matrix_calculation(A11, A22, "+"), matrix_calculation(B11, B22, "+"))
        ct += ct_temp
        P6, ct_temp = strassen_multiply(matrix_calculation(A12, A22, "-"), matrix_calculation(B21, B22, "+"))
        ct += ct_temp
        P7, ct_temp = strassen_multiply(matrix_calculation(A11, A21, "-"), matrix_calculation(B11, B12, "+"))
        ct += ct_temp
        ct += 7

        # compute the submatices of final matrix C
        C11 = matrix_calculation(matrix_calculation(matrix_calculation(P5, P4, "+"), P2, "-"), P6, "+")
        C12 = matrix_calculation(P1, P2, "+")
        C21 = matrix_calculation(P3, P4, "+")
        C22 = matrix_calculation(matrix_calculation(matrix_calculation(P1, P5, "+"), P3, "-"), P7, "-")

        # assmble final matrix C
        C = matrix_assemble(C11, C12, C21, C22)
        return C, ct


def ordinary_multiply(A, B):
    """
        Implementing the ordinary strategy to do matrix multiplication.

        A: One of the input matrices
        B: Another input matrix
        Return:
            C: the product matrix C multiplied from A and B
            ct: counter for multiplication
    """

    # initiate counter for analyzing computational cost
    ct = 0

    # initialize final product Matrix C
    n = len(A)
    C = [[0]*n for i in range(n)]

    # iteratively calculate matrix C
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
                ct += 1
    return C, ct


A = [[1, 3, 9, 2], [7, 5, 6, 9], [1, 3, 4, 8], [7, 5, 6, 6]]
B = [[6, 8, 3, 4], [4, 2, 1, 7], [1, 3, 4, 8], [7, 5, 6, 6]]

#numpy_product = np.dot(A, B)
#print(numpy_product)

#ordinary_product, ct = ordinary_multiply(A, B)
#matrix_print(ordinary_product)
# print(ct)

# strassen_product = strassen(np.matrix(A),np.matrix(B))
# print(strassen_product)

#strassen_product, ct = strassen_multiply(A, B)
#matrix_print(strassen_product)
# print(ct)

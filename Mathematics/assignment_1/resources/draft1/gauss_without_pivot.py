import numpy as np

# A = np.array([[10 ** -5, 1], [-2, 4]])
# b = np.array([[2], [10]])

A = np.array([[1, 10 ** 4],
              [-1, 2]])
b = np.array([[10 ** 4],
              [1]])

def forward_elim(A, b, n):
#calculates the forward part of Gaussian elimination.

    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i,row] / A[row,row]
            for j in range(row, n):
                A[i,j] = A[i,j] - factor * A[row,j]

            b[i] = b[i] - factor * b[row]

        # print("A = \n%s and b = %s" % (A,b))
    return A, b

def back_sub(A, b, n):
#back substitution and returns result

    x = np.zeros((n,1))
    x[n-1] = b[n-1] / A[n-1, n-1]
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - A[row,j] * x[j]
        x[row] = sums / A[row,row]
    return x

def gauss_elim(A, b):
#performs gaussian elimination without pivoting

    n = A.shape[0]
    #checks for zero diagonal elements
    if any(np.diag(A)==0):
        raise ZeroDivisionError(("Can't divide by 0")) #raise used to raise exception

    A, b = forward_elim(A, b, n)
    return back_sub(A, b, n)


x = gauss_elim(A, b)
print(x)
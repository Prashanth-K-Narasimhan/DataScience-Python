import sys
import numpy as np
from sigfig import round
from decimal import Decimal, ROUND_HALF_UP
from math import ceil, floor, pow

def Cal_forward_elimination_pivot(D, g):
    A = np.array((D), dtype=float)
    f = np.array((g), dtype=float)
    n = len(f)
    for k in range(0, n - 1):  # Loop through the columns of the matrix

        # if np.abs(A[i,i])==0:
        m = k
        for j in range(k + 1, n):
            if np.abs(A[m, k]) < np.abs(A[j, k]):
                m = j;
        if A[m, k] == 0:
            sys.exit("No unique solution exists")
        else:
            A[[m, k]] = A[[k, m]]
            f[[m, k]] = f[[k, m]]

        if A[n - 1, n - 1] == 0:
            sys.exit("No unique solution exits")

        else:
            for j in range(k + 1, n):  # Loop through rows below diagonal for each column
                m = A[j, k] / A[k, k]
                A[j, :] = A[j, :] - m * A[k, :]
                f[j] = f[j] - m * f[k]
    return A, f

def Cal_forward_elimination_pivot_with_rounding(D, g, precision):
    A = np.array((D), dtype=float)
    A = np.around(A, precision)
    f = np.array((g), dtype=float)
    f = np.around(f, precision)
    n = len(f)
    # print("Input array:")
    # print("main array: ", A)
    # print("frequeny", f)

    for k in range(0, n - 1):  # Loop through the columns of the matrix
        # print("=============")
        # print("Interation ", k)
        # if np.abs(A[i,i])==0:
        m = k
        for j in range(k + 1, n):
            if np.abs(A[m, k]) < np.abs(A[j, k]):
                m = j;
        if A[m, k] == 0:
            sys.exit("No unique solution exists")
        else:

            print("----------------------")
            print(A[[m, k]])
            A[[m, k]] = A[[k, m]]

            f[[m, k]] = f[[k, m]]


        if A[n - 1, n - 1] == 0:
            sys.exit("No unique solution exits")

        else:
            for j in range(k + 1, n):  # Loop through rows below diagonal for each column
                m = A[j, k] / A[k, k]
                print(m)
                m = round(float(m), sigfigs=precision)
                print(round(float(m), sigfigs=precision))

                A[j, :] = A[j, :] - m * A[k, :]
                f[j] = f[j] - m * f[k]
                A = np.around(A, 4)
                f = np.around(f, 4)

    return A, f

def back_substitution(A, f):
    n = f.size
    x = np.zeros(n)  # Initialize the solution vector, x, to zero
    x[n - 1] = f[n - 1] / A[n - 1, n - 1]  # Solve for last entry first
    for i in range(n - 2, -1, -1):  # Loop from the end to the beginning
        sum_ = 0
        for j in range(i + 1, n):  # For known x values, sum and move to rhs
            sum_ = sum_ + A[i, j] * x[j]
        x[i] = (f[i] - sum_) / A[i, i]
    return x

def back_substitution_with_precision(A, f, precision):
    n = f.size
    x = np.zeros(n)  # Initialize the solution vector, x, to zero
    x[n - 1] = f[n - 1] / A[n - 1, n - 1]  # Solve for last entry first
    for i in range(n - 2, -1, -1):  # Loop from the end to the beginning
        sum_ = 0
        for j in range(i + 1, n):  # For known x values, sum and move to rhs
            sum_ = sum_ + A[i, j] * x[j]
        x[i] = (f[i] - sum_) / A[i, i]
    return np.around(x, 4)

# A = np.random.randint(100, size=(2,2))
# f = np.random.randint(100, size=(2,1))
# A = np.array([[-3,6,-9],[1,-4,3],[2,5,-7]])
# f = np.array([-46.725,19.571,-20.073])

# A = np.array([[35, 3], [89, 67]])
# f = np.array([83, 9])

# Ax=b

A = np.array([[4.03,2.16],
              [6.21,3.35]])

f = np.array([[-4.61],
              [-7.19]])

# A = np.array([[10 ** -4, 1],
#               [-1, 2]])
# f = np.array([[1],
#            [1]])

# A = np.array([[0,6,13],[6,0,-8],[13,-8,0]])
# f = np.array([137.86,-85.88,178.54])


# A = 10 * np.random.randn(2, 2)
# print(f'Mat A : \n {A}', end="\n\n")
#
# f = 10 * np.random.randn(2, 1)
# print(f'Mat B : \n {f}')

for d in range(2, 6):
    precision = d
    B, g = Cal_forward_elimination_pivot_with_rounding(A, f, precision)
    # print(B)
    # print(g)
    x = back_substitution_with_precision(B, g, precision)
    print("Answer : ", x)




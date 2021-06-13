import numpy as np

def Cal_LU_pivot(D, g, d):
    A = np.array((D), dtype=float)
    f = np.array((g), dtype=float)
    n = len(f)
    for i in range(0, n - 1):  # Loop through the columns of the matrix

        if np.abs(A[i, i]) == 0:
            for k in range(i + 1, n):
                if np.abs(A[k, i]) > np.abs(A[i, i]):
                    A[[i, k]] = A[[k, i]]  # Swaps ith and kth rows to each other
                    f[[i, k]] = f[[k, i]]
                    break

        for j in range(i + 1, n):  # Loop through rows below diagonal for each column
            m = A[j, i] / A[i, i]
            m = np.round(m, d - int(np.floor(np.log10(abs(m)))) - 1)
            print("ratio:", m)
            A[j, :] = A[j, :] - m * A[i, :]
            f[j] = f[j] - m * f[i]
    return A, f

def Back_Subs(A,f):
    n = f.size
    x = np.zeros(n) # Initialize the solution vector, x, to zero
    x[n-1] = f[n-1]/A[n-1,n-1] # Solve for last entry first
    for i in range(n-2,-1,-1): # Loop from the end to the beginning
        sum_ = 0
        for j in range(i+1,n): # For known x values, sum and move to rhs
            sum_ = sum_ + A[i,j]*x[j]
            x[i] = (f[i] - sum_)/A[i,i]
    return x

def gauss_elimination_with_pivot(A, f, d):
    print("System of equations:")
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print("[{}] = [{}]".format(" + ".join(row), f[i]))
    B, g = Cal_LU_pivot(A, f, d)
    X = Back_Subs(B, g)
    return X

A = np.array([[4.03,2.16],
              [6.21,3.35]])

f = np.array([[-4.61],
              [-7.19]])

precision = 3
x = gauss_elimination_with_pivot(A, f, precision)
print("Answer : ", x)
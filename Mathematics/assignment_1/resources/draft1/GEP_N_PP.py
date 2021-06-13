import numpy as np

def GENP(A, b):
    '''
    Gaussian elimination with no pivoting.
    % input: A is an n x n nonsingular matrix
    %        b is an n x 1 vector
    % output: x is the solution of Ax=b.
    % post-condition: A and b have been modified.
    '''
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in range(n-1):
        for row in range(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #the only one in this column since the rest are zero
            A[row][pivot_row] = multiplier
            for col in range(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[pivot_row]
    # print(A)
    # print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x


def GEPP(A, b, doPricing=True):
    '''
    Gaussian elimination with partial pivoting.

    input: A is an n x n numpy matrix
           b is an n x 1 numpy array
    output: x is the solution of Ax=b
            with the entries permuted in
            accordance with the pivoting
            done by the algorithm
    post-condition: A and b have been modified.
    '''
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between" +
                         "A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the
    # upper right triangle, we also use k for indicating the k-th diagonal
    # column index.

    # Elimination
    for k in range(n - 1):
        if doPricing:
            # Pivot
            maxindex = abs(A[k:, k]).argmax() + k
            if A[maxindex, k] == 0:
                raise ValueError("Matrix is singular.")
            # Swap
            if maxindex != k:
                A[[k, maxindex]] = A[[maxindex, k]]
                b[[k, maxindex]] = b[[maxindex, k]]
        else:
            if A[k, k] == 0:
                raise ValueError("Pivot element is zero. Try setting doPricing to True.")
        # Eliminate
        for row in range(k + 1, n):
            multiplier = A[row, k] / A[k, k]
            A[row, k:] = A[row, k:] - multiplier * A[k, k:]
            b[row] = b[row] - multiplier * b[k]
    # Back Substitution
    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        x[k] = (b[k] - np.dot(A[k, k + 1:], x[k + 1:])) / A[k, k]
    return x

if __name__ == "__main__":
    # A = np.array([[10 ** -5, 1], [-2, 4]])
    # b = np.array([[2], [10]])

    A = np.array([[1, 10**4],
                  [-1, 2]])
    b = np.array([[10**4],
                  [1]])


    condition_numbers = np.linalg.cond(A)

    print(condition_numbers)

    print(GENP(np.copy(A), np.copy(b)))
    print(GEPP(A,b))
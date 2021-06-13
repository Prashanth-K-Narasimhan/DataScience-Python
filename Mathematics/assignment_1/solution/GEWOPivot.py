import numpy as np

def forward_elimination(A, b, n):
    """
    Calculates the forward part of Gaussian elimination.
    """
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i,row] / A[row,row]
            for j in range(row, n):
                A[i,j] = A[i,j] - factor * A[row,j]

            b[i] = b[i] - factor * b[row]

        print('A = \n%s and b = %s' % (A,b))
    return A, b

def forward_elimination_with_precision(A, b, n, precision):
    """
    Calculates the forward part of Gaussian elimination.
    """
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i,row] / A[row,row]
            for j in range(row, n):
                A[i,j] = np.around(A[i,j] - factor * A[row,j], precision)

            b[i] = np.around(b[i] - factor * b[row], precision)

        print('A = \n%s and b = %s' % (A,b))
    return A, b


def back_substitution(a, b, n):
    """"
    Does back substitution, returns the Gauss result.
    """
    x = np.zeros((n,1))
    x[n-1] = b[n-1] / a[n-1, n-1]
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row,j] * x[j]
        x[row] = sums / a[row,row]
    return x

def back_substitution_with_precision(a, b, n, precision):
    """"
    Does back substitution, returns the Gauss result.
    """
    x = np.zeros((n,1))
    x[n-1] = np.around(b[n-1] / a[n-1, n-1], precision)
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = np.around(sums - a[row,j] * x[j], precision)
        x[row] = np.around(sums / a[row,row],precision)
    return x

def gauss(A, b):
    """
    This function performs Gauss elimination without pivoting.
    """
    n = A.shape[0]

    # Check for zero diagonal elements
    if any(np.diag(A)==0):
        raise ZeroDivisionError(('Division by zero will occur; '
                                  'pivoting currently not supported'))

    A, b = forward_elimination(A, b, n)
    return back_substitution(A, b, n)

def gausswith_precision(A, b, precision):
    """
    This function performs Gauss elimination without pivoting.
    """
    n = A.shape[0]

    # Check for zero diagonal elements
    if any(np.diag(A)==0):
        raise ZeroDivisionError(('Division by zero will occur; '
                                  'pivoting currently not supported'))

    A, b = forward_elimination_with_precision(A, b, n, precision)

    print(A)
    print(b)

    return back_substitution_with_precision(A, b, n, precision)

# Main program starts here
if __name__ == '__main__':
    A = np.array([[10 ** -4, 1],
                  [-1, 2]])
    f = np.array([[1],
                  [1]])
    x = gausswith_precision(A, f, 4)
    print('Gauss result is x = \n %s' % x)
import numpy as np
from sigfig import round

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

        #print('A = \n%s and b = %s' % (A,b))
    return A, b

def forward_elimination_with_precision(A, b, n, precision):
    """
    Calculates the forward part of Gaussian elimination.
    """
    for row in range(0, n-1):
        for i in range(row+1, n):
            factor = A[i,row] / A[row,row]

            print(factor)
            factor = round(float(factor), sigfigs=precision)
            print(round(float(factor), sigfigs=precision))

            for j in range(row, n):
                A[i,j] = np.around(A[i,j] - factor * A[row,j], 4)

            b[i] = np.around(b[i] - factor * b[row], 4)

        #print('A = \n%s and b = %s' % (A,b))
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
    x[n-1] = b[n-1] / a[n-1, n-1]
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row,j] * x[j]
        x[row] = sums / a[row,row]
    return np.around(x, 4)

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
    n = 2

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
    '''
    A = np.array([[10 ** -4, 1],
                  [-1, 2]])
    f = np.array([[1],
                  [1]])
    x = gausswith_precision(A, f, 4)
    #print('Gauss result is x = \n %s' % x)
    '''

    # matA = 10 * np.random.randn(2, 2)
    # print(f'Mat A : \n {matA}', end= "\n\n")
    #
    # matf = 10 * np.random.randn(2, 1)
    # print(f'Mat B : \n {matf}')

    matA = np.array([[4.03,2.16],
                  [6.21,3.35]])

    matf = np.array([[-4.61],
                  [-7.19]])

    for d in range(2, 6):
        precision = d
        print(d)
        x = gausswith_precision(matA, matf, precision)
        print("Answer : ", x)
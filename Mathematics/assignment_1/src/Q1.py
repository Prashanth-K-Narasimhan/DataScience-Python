import numpy as np


def random_matrix(sig_digits):
    """
    Generates a Random 2x3 augmented matrix which adheres to the Linear Equation form Ax = B

    :param sig_digits: Integer
    :return: Numpy Array
    """

    # Random Matrix is multiplied with Pi to get the decimal values
    np.random.seed(24)
    for _ in range(0, 13):
        A = np.random.randint(low=0, high=99, size=(2, 3)) * np.pi
        if A[0][0] < A[1][0]:
            break
    print("Initial Matrix")
    print(A)

    return A


def gauss_elimination_without_pivoting(sig_digits):
    """
    This function deals with gaussian elimination without pivoting

    :param sig_digits: Significant Digits
    :return: Gaussian Eliminated Matrix
    """

    # Generating a Random Matrix
    # A = random_matrix(sig_digits)

    A = np.array([[1, 10 ** 4, 10 ** 4],
                  [-1, 2, 1]])

    # Making A[0][0] == 1
    A[0] = (A[0] / A[0][0]).round(decimals=sig_digits)

    # Making A[1][0] == 0
    if A[1][0] == 0.:
        pass
    else:
        A[1] = (A[1] - A[1][0] * A[0]).round(decimals=sig_digits)

    # Making A[0][1] == 0
    if A[0][1] == 0:
        pass
    else:
        A[0] = (A[0] - (A[1] * (A[0][1] / A[1][1]))).round(decimals=sig_digits)

    # Making A[1][1] == 1
    A[1] = (A[1] / A[1][1]).round(decimals=sig_digits)

    # Aesthetic
    A[1][0] = abs(A[1][0])

    print("----------------------")
    print("Final Matrix")
    print(A)


#sig_digit = int(input("Enter the Significant Digit: "))
gauss_elimination_without_pivoting(sig_digits=6)


def gauss_elimination_with_pivoting(sig_digits):

    # Generating a Random Matrix with Decimal places
    # A = random_matrix(sig_digits)

    A = np.array([[1, 10 ** 4, 10 ** 4],
                  [-1, 2, 1]])
    # Exchange Rows A[0] and A[1]
    A[[0, 1]] = A[[1, 0]]

    print("----------------------")
    print("Matrix after Partial Pivoting")
    print(A)

    # Making A[0][0] == 1
    A[0] = (A[0] / A[0][0]).round(decimals=sig_digits)

    # Making A[1][0] == 0
    if A[1][0] == 0.:
        pass
    else:
        A[1] = (A[1] - A[1][0] * A[0]).round(decimals=sig_digits)

    # Making A[0][1] == 0
    if A[0][1] == 0:
        pass
    else:
        A[0] = (A[0] - (A[1] * (A[0][1] / A[1][1]))).round(decimals=sig_digits)

    # Making A[1][1] == 1
    A[1] = (A[1] / A[1][1]).round(decimals=sig_digits)

    # Aesthetic
    A[1][0] = abs(A[1][0])

    print("----------------------")
    print("Final Matrix")
    print(A)


gauss_elimination_with_pivoting(sig_digits=2)
gauss_elimination_without_pivoting(sig_digits=2)
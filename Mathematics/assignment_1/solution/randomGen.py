import pandas as pd
import numpy as np

# np.random.uniform(-100.0, 100.0)

'''
shape = 3
elements = shape**2

random_array = np.round(np.random.uniform(-100, 100, shape**2), 2)

print(random_array.reshape(shape,shape))

for i in range(0, elements, shape):
    indice =
    print(i)
print(random_array)
'''

import numpy as np
from scipy.linalg import eigvals


def diagonal_dominant():
    """
    Check the Diagonal Dominance Condition.
    If true then it breaks the loop and returns the Diagonally Dominant Matrix

    :return A: Diagonally Dominant Matrix
    :return b: RHS Matrix
    """
    np.random.seed(48)
    for _ in range(0, 99999):
        # Multiplied with pi to get decimals
        A = (np.random.randint(low=0, high=9, size=(3, 3)) * np.pi).round(decimals=4)

        # Diagonal Dominance Check
        if (A[0][0] > (abs(A[0][1]) + abs(A[0][2]))) and (A[1][1] > (abs(A[1][0]) + abs(A[1][2]))) and (A[2][2] > (abs(A[2][0]) + abs(A[2][1]))):
            break

    print("Initial Matrix before Normalization")
    print(A)

    # Generate b
    b = (np.random.randint(0, 99, (3, 1)) * np.pi).round(decimals=4)
    print("----------------------------")
    print("b Matrix")
    print(b)

    return A, b


def diagonal_not_dominant():
    """
    Check the Diagonal Dominance Condition.
    If true then simply skip the iteration. If false, it breaks the loop
    and returns the Diagonally Not Dominant Matrix
    :return A: Diagonally Not Dominant Matrix
    :return b: RHS Matrix
    """
    np.random.seed(120)
    for _ in range(0, 99999):
        A = (np.random.randint(low=0, high=9, size=(3, 3)) * np.pi).round(decimals=4)

        # Diagonal Dominance Check
        if (A[0][0] > (abs(A[0][1]) + abs(A[0][2]))) and (A[1][1] > (abs(A[1][0]) + abs(A[1][2]))) and (A[2][2] > (abs(A[2][0]) + abs(A[2][1]))):
            pass
        else:
            break

    print("Initial Matrix before Normalization")
    print(A)

    # Generate b
    b = (np.random.randint(0, 99, (3, 1)) * np.pi).round(decimals=4)
    print("----------------------------")
    print("b Matrix")
    print(b)

    return A, b


def random_matrix(switch_number=1):
    """
    Generates a Random Normalized 3x3 matrix and checks for Diagonal Dominance Condition.
    Finally augments the randomly generated "b".

    The switch number is set to one to call the Diagonally Dominant Check function.

    :parameter switch_number: Integer
    :return A: Normalized Array
    :return b: RHS Matrix
    """

    # This condition works as a switch to experiment with both Diagonally Dominant and
    # not Dominant Matrices
    if switch_number == 1:
        A, b = diagonal_dominant()
    else:
        A, b = diagonal_not_dominant()

    # Normalizing Matrix
    for i in range(0, 3):
        b[i] = (b[i] / A[i][i]).round(decimals=4)
        A[i] = (A[i] / A[i][i]).round(decimals=4)

    print("-------------------------")
    print("Matrix after Normalization")
    print(A)

    return A, b

R = np.matrix([[2.5, 2.9], [2.3, 2.7]])
m = R.shape[0]
n = R.shape[1]
A = np.matrix(np.zeros(shape=(n, n)))
B = np.matrix(np.zeros(shape=(m, n)))

from numpy.random import RandomState

np.set_printoptions(suppress=True)
random_state = RandomState(1240)

diag_dom_condition = False

# Generate diagonally dominant matrix
while diag_dom_condition != True:
    a = 20 * random_state.rand(3, 4)
    a = np.around(a, decimals=4)
    diag_dom_condition = (np.abs(a[0][0]) > np.abs(a[0][1]) + np.abs(a[0][2])) and \
                         (np.abs(a[1][1]) > np.abs(a[1][0]) + np.abs(a[1][2])) and \
                         (np.abs(a[2][2]) > np.abs(a[2][0]) + np.abs(a[2][1]))

print(a)


print(random_matrix(1))
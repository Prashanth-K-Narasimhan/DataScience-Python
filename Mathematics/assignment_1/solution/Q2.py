import numpy as np
from scipy.linalg import eigvals


def diagonal_dominant():
    """
    Check the Diagonal Dominance Condition.
    If true then it breaks the loop and returns the Diagonally Dominant Matrix

    :return A: Diagonally Dominant Matrix
    :return b: RHS Matrix
    """
    np.random.seed(321)
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
    np.random.seed(232)
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


def gauss_jacobi():
    """
    Performs the Gauss Jacobi Iterative Method.

    :return None: Prints out the Iteration Number and the corresponding X Matrix
    """

    # Normalized Random Matrix
    A, b = random_matrix()

    # Identity Matrix
    I = np.identity(3, dtype=float)

    difference = I - A

    # Spectral Radius Check
    spectral_radius = max(abs(eigvals(difference)))

    if spectral_radius < 1:
        print("Matrix will Converge")
        print("--------------------------")
        print("Jacobi Iterations")
        print("--------------------------")
        # Jacobi Iterations

        # Assume X1, X2, X3 = 0
        X = np.zeros(shape=(3, 1))

        for i in range(1, 19):
            X = (b + np.dot(difference, X)).round(decimals=4)
            print(f"Iteration {i}: {X}")

            print("------------")

    else:
        print("Matrix will not Converge")
        print("Exiting the Condition")


def gauss_seidel():
    """
    Performs the Gauss Seidel Iterative Method.

    :return None: Prints out the Iteration Number and the corresponding matrix
    """

    # Normalized Random Matrix
    A, b = random_matrix()

    # Decompose A to I, L, U
    I = np.identity(3, dtype=float)

    L = np.tril(A)
    for i in range(0, 3):
        L[i][i] = L[i][i] - 1

    U = np.triu(A)
    for i in range(0, 3):
        U[i][i] = U[i][i] - 1

    I_L_inv = np.linalg.inv(I + L)  # (I + L) Inverse

    convergence = np.dot(-I_L_inv, U) # C = -(I + L) Inverse * U

    print("----------------------------")
    print("Convergence Matrix")
    print(convergence)

    # Frobenius Norm
    if np.linalg.norm(convergence) < 1:
        print("Matrix will converge")
        print("------------------------")
        print("Seidel Iterations")
        print("------------------------")

        # Seidel Iterations

        # Assume X0, X1, X2 = 0
        X = np.zeros(shape=(3, 1))

        for i in range(1, 19):
            # X = Cx + (I + L) Inverse * b
            X = (np.dot(convergence, X) + np.dot(I_L_inv, b)).round(decimals=4)
            print(f"Iteration {i}:{X} ")

    else:
        print("Matrix does not converge")
        print("Exiting the Condition")


def gauss_jacobi_divergence():
    """
    Shows the Divergence for a Non Diagonally Dominant Matrix.

    :return None: Prints out the Divergence values along with Iteration Number
    """

    # Normalized Random Matrix
    A, b = random_matrix(2)

    # Identity Matrix
    I = np.identity(3, dtype=float)

    difference = I - A

    # Spectral Radius Check
    spectral_radius = max(abs(eigvals(difference)))

    # Jacobi Iterations

    # Assume X1, X2, X3 = 0
    X = np.zeros(shape=(3, 1))

    for i in range(1, 19):
        X = (b + np.dot(difference, X)).round(decimals=4)
        print(f"Iteration {i}: {X}")
        print("------------")


def gauss_seidel_divergence():
    """
    Shows the Divergence for a Non Diagonally Dominant Matrix in Gauss Seidel Method
    :return:
    """
    # Normalized Random Matrix
    A, b = random_matrix(2)

    # Decompose A to I, L, U
    I = np.identity(3, dtype=float)

    L = np.tril(A)
    for i in range(0, 3):
        L[i][i] = L[i][i] - 1

    U = np.triu(A)
    for i in range(0, 3):
        U[i][i] = U[i][i] - 1

    I_L_inv = np.linalg.inv(I + L)  # (I + L) Inverse

    convergence = np.dot(-I_L_inv, U) # C = -(I + L) Inverse * U

    print("----------------------------")
    print("Convergence Matrix")
    print(convergence)

    # Seidel Iterations

    # Assume X0, X1, X2 = 0
    X = np.zeros(shape=(3, 1))

    for i in range(1, 19):
        # X = Cx + (I + L) Inverse * b
        X = (np.dot(convergence, X) + np.dot(I_L_inv, b)).round(decimals=4)
        print(f"Iteration {i}:{X} ")


option = input("Enter 1 for Gauss-Jacobi. \n"
               "Enter 2 for Gauss-Seidel. \n"
               "Enter 3 for Gauss-Jacobi Divergence. \n"
               "Enter 4 for Gauss-Seidel Divergence: \n")

if option == "1":
    gauss_jacobi()
elif option == "2":
    gauss_seidel()
elif option == "3":
    gauss_jacobi_divergence()
elif option == "4":
    gauss_seidel_divergence()
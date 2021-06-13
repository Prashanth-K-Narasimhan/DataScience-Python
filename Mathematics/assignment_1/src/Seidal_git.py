# %% md
# %%

import numpy as np


# %%

def checkDiagnolDominant(a):
    # Find diagonal coefficients
    diag = np.diag(np.abs(a))

    # Find row sum without diagonal
    off_diag = np.sum(np.abs(a), axis=1) - diag

    if np.all(diag > off_diag):
        print('matrix is diagonally dominant')
        return True
    else:
        print('NOT diagonally dominant')
        return False


# %%

def gauss_seidel(A, b, tolerance=0.01, max_iterations=10000):
    x = np.zeros_like(b, dtype=np.float)

    # if checkDiagnolDominant(a) == False:
    #     return False

    # Iterate
    for k in range(max_iterations):

        x_old = x.copy()

        # Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]

        print(x[0], " ", x[1], " ", x[2])

        # Stop condition
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            break

    return x


# %%

x = [0, 0, 0]
# a = np.array([[4, 1, 2],[3, 5, 1],[1, 1, 3]])
# b = np.array([4,7,3])

a = np.random.uniform(0, 9, size=(3, 3))
a = a * 10000 // 1 / 10000
b = np.random.uniform(0, 9, size=(3, 1))
b = b * 10000 // 1 / 10000
print("Input matrix : ", a)
print("freq:", b)
print("======")
# generate diagnolly dominant
for i in range(a.shape[0]):
    d = a[i][i]
    a[i][i] = sum(a[i]) - d + 1
gauss_seidel(a, b)

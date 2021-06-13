# %%

from math import ceil, floor, pow
import numpy as np

# %%

def Round_off(N, n):
    b = N
    c = floor(N)
    i = 0;
    while (b >= 1):
        b = b / 10
        i = i + 1
    d = n - i
    b = N
    b = b * pow(10, d)
    e = b + 0.5
    if (float(e) == float(ceil(b))):
        f = (ceil(b))
        h = f - 2
        if (h % 2 != 0):
            e = e - 1
    j = floor(e)
    m = pow(10, d)
    j = j / m
    return j


# %%

def Gauss_Elimination_With_Pivoting(Augumented_matrix, significant_digits):
    num_rows, num_cols = Augumented_matrix.shape
    solution = np.arange(num_rows)
    solution.fill(0)
    solution = np.array((solution), dtype=float)
    intermediate_matrix = Augumented_matrix.copy()

    # Forward Elimination Begins Below
    for k in range(num_rows - 1):
        m = k
        for j in range(k + 1, num_rows):
            if (abs(Augumented_matrix[m][k]) < abs(Augumented_matrix[j][k])):
                m = j
        if Augumented_matrix[m][k] == 0:
            print("No Unique Solution Exists")
            exit()
        else:
            Augumented_matrix[[m, k]] = Augumented_matrix[[k, m]]

        if Augumented_matrix[num_rows - 1][num_rows - 1] == 0:
            print("No Unique Solution Exists")
            exit()
        else:
            for j in range(k + 1, num_rows):
                q = Round_off(Augumented_matrix[j][k] / Augumented_matrix[k][k], significant_digits)
                print(q)
                Augumented_matrix[j][k] = 0
                for p in range(k + 1, num_cols):
                    Augumented_matrix[j][p] = Round_off(Augumented_matrix[j][p] - (q * Augumented_matrix[k][p]),
                                                        significant_digits)
    # Forward Elimination Ends above

    # backward Subsitution Begins Below
    solution[num_rows - 1] = Augumented_matrix[num_rows - 1][num_cols - 1] / Augumented_matrix[num_rows - 1][
        num_rows - 1]
    for i in range(num_rows - 2, -1, -1):
        z = 0
        for j in range(i + 1, num_rows):
            y = Round_off(Augumented_matrix[i][j] * solution[j], significant_digits)
            z = Round_off(z + y, significant_digits)
        solution[i] = (Augumented_matrix[i][num_cols - 1] - z) / Augumented_matrix[i][i]
    # backward Subsitution Ends above

    print("The solution with partial pivoting is ", solution)
    Augumented_matrix = intermediate_matrix.copy()


# %%

def Gauss_Elimination_Without_Pivoting(Augumented_matrix, significant_digits):
    num_rows, num_cols = Augumented_matrix.shape
    solution = np.arange(num_rows)
    solution.fill(0)
    solution = np.array((solution), dtype=float)
    intermediate_matrix = Augumented_matrix.copy()

    # Forward Elimination Begins Below
    for k in range(num_rows - 1):
        m = k
        for j in range(k + 1, num_rows):
            if (abs(Augumented_matrix[m][k]) < abs(Augumented_matrix[j][k])):
                m = j
        if Augumented_matrix[m][k] == 0:
            print("No Unique Solution Exists")
            exit()
        elif Augumented_matrix[k][k] == 0:
            Augumented_matrix[[m, k]] = Augumented_matrix[[k, m]]

        if Augumented_matrix[num_rows - 1][num_rows - 1] == 0:
            print("No Unique Solution Exists")
            exit()
        else:
            for j in range(k + 1, num_rows):
                q = Round_off(Augumented_matrix[j][k] / Augumented_matrix[k][k], significant_digits)
                print(q)
                Augumented_matrix[j][k] = 0
                for p in range(k + 1, num_cols):
                    Augumented_matrix[j][p] = Round_off(Augumented_matrix[j][p] - (q * Augumented_matrix[k][p]),
                                                        significant_digits)
    # Forward Elimination Ends above

    # backward Subsitution Begins Below
    solution[num_rows - 1] = Augumented_matrix[num_rows - 1][num_cols - 1] / Augumented_matrix[num_rows - 1][
        num_rows - 1]
    for i in range(num_rows - 2, -1, -1):
        z = 0
        for j in range(i + 1, num_rows):
            y = Round_off(Augumented_matrix[i][j] * solution[j], significant_digits)
            z = Round_off(z + y, significant_digits)
        solution[i] = (Augumented_matrix[i][num_cols - 1] - z) / Augumented_matrix[i][i]
    # backward Subsitution Ends above

    print("The solution without partial pivoting is ", solution)
    Augumented_matrix = intermediate_matrix.copy()


# %%


# Random matrix generator and Augumented matrix generator begins Below
def random_generator(order_of_matrix):
    LHS_Coefficients = np.random.randn(order_of_matrix, order_of_matrix)
    RHS_Coefficients = np.random.randn(order_of_matrix, 1)
    Augumented_matrix = np.column_stack((LHS_Coefficients, RHS_Coefficients))
    Augumented_matrix = np.array((Augumented_matrix), dtype=float)
    print(Augumented_matrix)
    return Augumented_matrix


# Random matrix generator and Augumented matrix generator Ends Above


# %%

# Augumented_matrix = random_generator(2)

# %%

# Augumented_matrix[0][0]=0.0004
# Augumented_matrix[0][1]=1.402
# Augumented_matrix[1][0]=0.4003
# Augumented_matrix[1][1]=-1.502
# Augumented_matrix[0][2]=1.406
# Augumented_matrix[1][2]=2.501

# Augumented_matrix[0][0]=0.18654257
# Augumented_matrix[0][1]=-0.17774015
# Augumented_matrix[1][0]=-0.28855266
# Augumented_matrix[1][1]=0.47578736
# Augumented_matrix[0][2]=-0.98182335
# Augumented_matrix[1][2]=0.43773786

# Augumented_matrix[0][0]=-0.9815
# Augumented_matrix[0][1]=0.0661
# Augumented_matrix[0][2]=0.3732
# Augumented_matrix[0][3]=0.15291635
# Augumented_matrix[1][0]=0.2709
# Augumented_matrix[1][1]=-1.152
# Augumented_matrix[1][2]=0.2068
# Augumented_matrix[1][3]=0.98563742
# Augumented_matrix[2][0]=0.3125
# Augumented_matrix[2][1]=-0.4523
# Augumented_matrix[2][2]=-1.2511
# Augumented_matrix[2][3]=0.58006576


# %%

# Augumented_matrix[0][0]=0.0004
# Augumented_matrix[0][1]=1.402
# Augumented_matrix[1][0]=0.4003
# Augumented_matrix[1][1]=-1.502
# Augumented_matrix[0][2]=1.406
# Augumented_matrix[1][2]=2.501
# Gauss_Elimination_Without_Pivoting(Augumented_matrix, 4)

# %%

matA = np.array([[4.03,2.16],
              [6.21,3.35]])

matf = np.array([[-4.61],
              [-7.19]])

Augumented_matrix = np.column_stack((matA, matf))
print(type(Augumented_matrix))
Augumented_matrix = np.array((Augumented_matrix), dtype=float)

print(Augumented_matrix)

Gauss_Elimination_With_Pivoting(Augumented_matrix, 4)
Gauss_Elimination_Without_Pivoting(Augumented_matrix, 4)
# print(Round_off(137.77, 3))
# print(round(137.77, 3))

# %%



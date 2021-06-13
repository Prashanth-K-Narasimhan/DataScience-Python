import numpy as np

A = np.array([[10**-5,1],[-2,4]])
b = np.array([[2],[10]])
print(A)
print(b)
print(np.concatenate((A, b), axis=1))
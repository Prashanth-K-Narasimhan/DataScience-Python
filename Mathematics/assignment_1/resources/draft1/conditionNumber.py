import numpy as np
import scipy.linalg as la

# A = np.random.rand(2, 2)
# b = np.random.rand(2, 1)

A = [[10**-5,1],[-2,4]]
b = [[2],[10]]
condition_numbers = np.linalg.cond(A)

print(f'Matrix A : \n'
      f' {A}')
print(f'Matrix B : \n'
      f' {b}')

print(f'condition number of the randomly gerarated matrix A is : {condition_numbers} ')

x = la.solve(A,b)
print(x)
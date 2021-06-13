'''
Method: Gauss-Seidel Iterative
Section: Systems of Linear Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_6_05.py
Date: Aug. 6, 2017
''' 
import numpy as np
a = np.array([[8, 2, 4],
           [3, 5, 1],
           [2, 1, 4]],float)
b = np.array([-16, 4, -12], float)
(n,) = np.shape(b)
x = np.full(n, 1.0, float) # initial value of x is 1.0
xdiff = np.empty(n, float)
iterlimit = 100
tolerance = 1.0e-6

# iterations:
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i, j]*x[j]
        xnew = -1/a[i,i] * (s - b[i])
        xdiff = abs(xnew - x[i])
        x[i] = xnew
    if(xdiff < tolerance).all():
        break

print('Number of iterations: %d '% (iteration+1))
print('The solution of the system:')
print(x)




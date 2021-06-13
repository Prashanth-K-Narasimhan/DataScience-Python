'''
Method: Jacobi Iterative
Section: Systems of Linear Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_6_04.py
Date: Aug. 6, 2017
''' 
from numpy import *
a = array([[8, 2, 4],
           [3, 5, 1],
           [2, 1, 4]],float)
b = array([-16, 4, -12], float)
(n,) = shape(b)
x = full(n, 1.0, float) 
xnew = empty(n, float)
iterlimit = 100
tolerance = 1.0e-6

# iterations:
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i, j]*x[j]
        xnew[i] = -1/a[i,i] * (s - b[i])
        print(xnew)
    if (abs(xnew - x) < tolerance).all():
        break
    else:
        x = copy(xnew)

print('Number of iterations: %d '% (iteration+1))
print('The solution of the system:')
print(x)




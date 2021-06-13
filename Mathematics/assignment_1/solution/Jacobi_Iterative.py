'''
Method: Jacobi Iterative
Section: Systems of Linear Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_6_04.py
Date: Aug. 6, 2017
''' 
import numpy as np
'''
a = array([[8, 2, 4],
           [3, 5, 1],
           [2, 1, 4]],float)
b = array([-16, 4, -12], float)
'''
# a = array([[8, 2, 4],
#            [3, 5, 1],
#            [2, 1, 4]],float)
# b = array([-16, 4, -12], float)


# condition = False
#
# while condition != True:
#     a = np.round(np.random.uniform(-100, 100, (3,3)), 4)
#     condition = (np.abs(a[0][0]) > np.abs(a[0][1]) + np.abs(a[0][2])) and \
#                          (np.abs(a[1][1]) > np.abs(a[1][0]) + np.abs(a[1][2])) and \
#                          (np.abs(a[2][2]) > np.abs(a[2][0]) + np.abs(a[2][1]))
#
# b = np.round(np.random.uniform(-100, 100, (3,)), 4)

a = np.array([[-81.82, - 20.9,  17.91],
              [-7.97, - 65.88, - 5.96],
              [-56.45, - 16.05, - 85.38]],float)
b = np.array([-72.4,  -97.78,  87.25], float)


print(f'Mat A : \n {a}', end="\n\n")
print(f'Mat B : \n {b}', end="\n\n")

(n,) = np.shape(b)
x = np.full(n, 1.0, float)
xnew = np.empty(n, float)
iterlimit = 100
tolerance = 1.0e-2

# iterations:
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i, j]*x[j]
        xnew[i] = -1/a[i,i] * (s - b[i])
    print(x)
    if (abs(xnew - x) < tolerance).all():
        print(iteration)
        break
    else:
        print(iteration)
        x = np.copy(xnew)

print('Number of iterations: %d '% (iteration+1))
print('The solution of the system:')
print(x)




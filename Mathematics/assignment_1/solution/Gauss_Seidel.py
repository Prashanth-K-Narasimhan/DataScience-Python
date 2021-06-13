'''
Method: Gauss-Seidel Iterative (Diagonal Dominance Condition)
Section: Systems of Linear Equations
Course: Programming Numerical Methods in Python
Instructor: Murad Elarbi
File Name: PNMP_6_06.py
Date: Aug. 6, 2017
''' 
import numpy as np
'''
a = np.array([[8, 2, 4],
           [3, 5, 1],
           [2, 1, 4]],float)
b = np.array([-16, 4, -12], float)
'''
condition = True

while condition != False:
    a = np.round(np.random.uniform(-100, 100, (3,3)), 4)
    condition = (np.abs(a[0][0]) > np.abs(a[0][1]) + np.abs(a[0][2])) and \
                         (np.abs(a[1][1]) > np.abs(a[1][0]) + np.abs(a[1][2])) and \
                         (np.abs(a[2][2]) > np.abs(a[2][0]) + np.abs(a[2][1]))

b = np.round(np.random.uniform(-100, 100, (3,)), 4)

# a = np.array( [[ 93.67,  -3.47,  -2.81],
#                [ 19.28, -51.,    26.41],
#                [ 61.93,  -2.06, -92.21]],float)
# b = np.array([-65.22,  69.2,   73.15], float)




# mine gauss
# a = np.array([[-39.4725, -52.2846, -72.002 ],
#               [-21.9554,  71.7555, -32.4064],
#               [-59.0722, -78.356,   38.6347]],float)
# b = np.array([-92.0478,  40.3656,  56.4648], float)

# a = np.array( [[ 65.1741,  21.2942,  -4.8958],
#                [ -9.9549,  91.7586,  43.3396],
#                [-21.1146,  22.9437, -47.5515]],float)
# b = np.array([ 34.0589, -84.0277, -15.961 ], float)

print(f'Mat A : \n {a}', end="\n\n")
print(f'Mat B : \n {b}', end="\n\n")

(n,) = np.shape(b)
print(n)
x = np.full(n, 1.0, float) # initial value of x is 1.0
xdiff = np.empty(n, float)
iterlimit = 100
tolerance = 1.0e-2

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
    print(x)
    if(xdiff < tolerance).all():
        print(iteration)
        break

print('Number of iterations: %d '% (iteration+1))
print('The solution of the system:')
print(x)




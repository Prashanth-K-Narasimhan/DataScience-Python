from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times                                                                                                                                                                          
    for i in range(N):
        x = (b - dot(R,x)) / D
        print(x)
    return x

def seidel(a, x ,b):
    #Finding length of a(3)       
    n = len(a)                   
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):        
        # temp variable d to store b[j]
        d = b[j]                  
          
        # to calculate respective xi, yi, zi
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]
        # updating the value of our solution        
        x[j] = d / a[j][j]
    # returning our updated solution           
    return x   

import numpy as np

n = int(input('Enter number of rows: '))

A = np.zeros((n,n))
b = np.zeros(n)
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        A[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
        
print("enter b values for %d equations",n)
for i in range(n):
    b[i]=np.float(input('b['+str(i)+']'))
    
guess=[1.0,1.0,1.0]

print("Jacobi iterations")
    
Jacobi = jacobi(A,b,N=25,x=guess)

x=[0,0,0]
    
print("Seidel iterations")

for i in range(0, 25):            
    x = seidel(A, x, b)
    #print each time the updated solution
    print(x) 
    
print("Jacobi=",Jacobi)
print("Seidel=",x)

################################################################################
# Gauss Elimination Script
#
# Purpose: This application impelments Gauss Elimination to solve a system.
# Users can choose to either use pivoting or not. This lab explores Gauss
# elimination algorithms.
#
# Author: Kevin Chen
# Contact: chenk106@mcmaster.ca
# GitHub: https://github.com/CNIVEK/GaussEliminationLab
#
################################################################################
import sys

import numpy as np

class Gauss:

    # Matrix intialization
    def start(self):
        # self.n = int(input("Enter the number of unknowns: "))
        self.n = 2
        self.A = np.zeros((self.n,self.n+1))    # Matrix creation, n xy n+1 size
        self.R = np.zeros((self.n,self.n+1))    # Multiplication matrix for columns
        self.x = np.zeros(self.n)               # Solution array

        # print("Enter augmented matrix coefficients:")
        # for i in range(self.n):
        #     for j in range (self.n+1):
        #         self.A[i][j] = input("matrix["+ str(i) +"]["+ str(j) +"] = ")

        self.A = np.array([[4.03, 2.16, -4.61],
                      [6.21, 3.35, -7.19]])

    # Applying Gauss Elimination
    def gaussElim(self):
        print(f"\nGuass Elimination\ninitial matrix:\n {self.A}")
        for i in range(self.n-1):  # loop over columns
            if self.A[i][i] == 0:
                sys.exit("pivor is zero, exiting")

            print(f"\ntransformation #{i+1}:")

            # Compute multipliers for current  column
            for j in range(i+1, self.n):
                self.R[j][i] = self.A[j][i] / self.A[i][i]

                print(f"row{j+1} = row{j+1} - {self.R[j][i]} * row{i+1}")

            # Apply transformation to remaining submatrix
            for k in range(self.n+1):
                for j in range(self.n):
                    self.A[j][k] = self.A[j][k] - self.R[j][i] * self.A[i][k]

            print(f"result:\n {self.A}")

    # Applying Gauss Elimination with Partial Pivoting
    def gaussElimPivot(self):
        print(f"\nGuass Elimination with Partial Pivoting\ninitial matrix:\n {self.A}")
        for i in range(self.n-1):  # loop over columns
            for p in range(i,self.n): # search for pivot
                if abs(self.A[p][i]) > abs(self.A[i][i]): # compare values for largest
                    self.A[[i,p]] = self.A[[p,i]]   # interchange rows
                    print(f"\ninterchange: r{i+1} <=> r{p+1} \nresult: \n {self.A}")
                else:
                    pass
            print(f"\ntransformation #{i+1}:")

            # Compute multipliers for current  column
            for j in range(i+1, self.n):
                self.R[j][i] = self.A[j][i] / self.A[i][i]

                print(f"row{j+1} = row{j+1} - {self.R[j][i]} * row{i+1}")

            # Apply transformation to remaining submatrix
            for k in range(self.n+1):
                for j in range(self.n):
                    self.A[j][k] = self.A[j][k] - self.R[j][i] * self.A[i][k]

            print(f"result:\n {self.A}")

    # Back substitution
    def backSub(self):
        self.x[self.n-1] = self.A[self.n-1][self.n] / self.A[self.n-1][self.n-1]
        for i in range(self.n-2,-1,-1):
            self.x[i] = self.A[i][self.n]
            for j in range(i+1, self.n):
                self.x[i] = self.x[i] - self.A[i][j] * self.x[j]
            self.x[i] = self.x[i] / self.A[i][i]

    # Display solution
    def displaySolution(self):
        print("\nSolution is: ")
        for i in range(self.n):
            print("x%d = %0.2f" %(i+1,self.x[i]))

g = Gauss()
g.start()
choice = input("\nEnter 1 for Pivoting, 0 for non-pivoting: ")
if choice == '1':
    g.gaussElimPivot()
else:
    g.gaussElim()
g.backSub()
g.displaySolution()
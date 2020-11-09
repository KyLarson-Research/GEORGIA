#Filename: matrix_KL1109020.py
#Author: Kyle Larson
#License: GNU General Public License V3 
#Purpose: to practice linear algebra operations in python
#/usr/local/opt/python@3.9/bin/python3.9
#import numpy as np
A = [[2,-2, 5], [-2, 1, -3], [1, 0, 1]]
#A = np.array(A)
print(A)
print(A[0])

r1 = A[0]

r2 = [A[1][0]+A[0][0], A[1][1]+A[0][1], A[1][2]+A[0][2]]

r3 = [A[2][0]-0.5*A[0][0], A[2][1]-0.5*A[0][1], A[2][2]-0.5*A[0][2]]


r3 = [r3[0]+r2[0], r3[1]+r2[1], r3[2]+r2[2]]

A = [r1, r2, r3]

A[1] = [A[1][0], A[1][1], A[1][2]-4*A[2][2]]

A[0] = [A[0][0], A[0][1], A[0][2]-10*A[2][2]]

A[0] = [A[0][0], A[0][1]-2*A[1][1], A[0][2]]

print(A)
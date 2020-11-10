#Filename: precourse_assessment_02.py
#Author: Kyle C. Larson
#License: GNU General Public License V3 
#Purpose: to demonstrate linear algebra operations in python
#/usr/local/opt/python@3.9/bin/python3.9
# to solve a set of equations use AX=K where X = A^(-1) * K , A^(-1) being the inverse matrix of A
import sympy as sp
b= [[3, 4], [2, 3]]
B = sp.Matrix(b)
print(B)
print(B.inv())
#to solve for the augmentation of [[6], [5]]
# B is A and [[6], [5]] is K
print(B.inv() * sp.Matrix([[6], [5]]))

#once more with a new example
c= [[1, 2, -3], [2, 3, -4], [-1, 0, 3]]
C= sp.Matrix(c)
print(C)
print(C.inv())
#to solve similarly
print(C.inv() * sp.Matrix([[-1], [2], [5]]) )
#Filename: precourse_assessment.py
#Author: Kyle C. Larson
#License: GNU General Public License V3 
#Purpose: to demonstrate linear algebra operations in python
#/usr/local/opt/python@3.9/bin/python3.9
import numpy as np
#row_echelon function only has been coppied from Vasily Mitch on 11/9/2020 
#from https://math.stackexchange.com/questions/3073083/how-to-reduce-matrix-into-row-echelon-form-in-python
def row_echelon(A):
	""" Return Row Echelon Form of matrix A """
	
	# if matrix A has no columns or rows,
	# it is already in REF, so we return itself
	r, c = A.shape
	if r == 0 or c == 0:
		return A

	# we search for non-zero element in the first column
	for i in range(len(A)):
		if A[i,0] != 0:
			break
	else:
		# if all elements in the first column is zero,
		# we perform REF on matrix from second column
		B = row_echelon(A[:,1:])
		# and then add the first zero-column back
		return np.hstack([A[:,:1], B])

	# if non-zero element happens not in the first row,
	# we switch rows
	if i > 0:
		ith_row = A[i].copy()
		A[i] = A[0]
		A[0] = ith_row

	# we divide first row by first element in it
	A[0] = A[0] / A[0,0]
	# we subtract all subsequent rows with first row (it has 1 now as first element)
	# multiplied by the corresponding element in the first column
	A[1:] -= A[0] * A[1:,0:1]

	# we perform REF on matrix from second row, from second column
	B = row_echelon(A[1:,1:])

	# we add first row and first (zero) column, and return
	return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])
#Example:
#A = np.array([[4, 7, 3, 8],
#              [8, 3, 8, 7],
#              [2, 9, 5, 3]], dtype='float')

#Consider the augmented matrix:
a = [ [3, 4, 1, 0], [2, 3, 0, 1] ]

A = np.array(a, dtype='float')
print('ref of the left half of A = ')
print(A)
print("is comes from the right of ")
print(row_echelon(A))
#print("therefore the inverse is")
print("")
A[0] = A[0] - (A[1]*A[0][1])
print("inverse comes from")
print(A)
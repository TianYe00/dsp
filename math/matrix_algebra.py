# Matrix Algebra

import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm
from numpy.linalg import matrix_rank
from numpy.linalg import matrix_power

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5]).reshape(1, 4)
v = np.array([3, 5, -1, 4]).reshape(1, 4)
w = np.array([1, 8, 0, 5]).reshape(4, 1)

#Q1
matrix_rank(A)
matrix_rank(B)
matrix_rank(C)
matrix_rank(D)
matrix_rank(u)
matrix_rank(w)

#Q2
u + v
u - v
alpha = 6
alpha * u
np.vdot(u, v)
norm(u)

#Q3
A + C
A - C.T
C.T +  3D
np.dot(B, A)
np.dot(B, A.T)

#Optional
np.dot(B, C)
np.dot(C, B)
matrix_power(B, 4)
np.dot(A, A.T)
np.dot(D.T, D)

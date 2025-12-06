import numpy as np
from scipy import linalg

A = np.array([[4,2,1],[0,1,-1],[2,3,5]], dtype=float)
detA = linalg.det(A)
invA = linalg.inv(A)
eigvals, eigvecs = linalg.eig(A)

print("Determinant:", detA)
print("Inverse:\n", invA)
print("Eigenvalues:", eigvals)

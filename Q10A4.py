import numpy as np
arr =[[2,1,3],[0,5,6],[7,8,9]]
det = np.linalg.det(arr)
print("Determinant:", det)
inv=np.linalg.inv(arr)
print("Inverse:\n", inv)
eigvals, eigvecs = np.linalg.eig(arr)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
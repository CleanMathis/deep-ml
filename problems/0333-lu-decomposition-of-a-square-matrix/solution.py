import numpy as np

def lu_decomposition(A: list) -> tuple:
	"""
	Perform LU decomposition on a square matrix using Doolittle's method.
	
	Args:
		A: Square matrix as a list of lists
	
	Returns:
		tuple: (L, U) where L is lower triangular with 1s on diagonal,
		       U is upper triangular, and A = L @ U
	"""
	A = np.array(A, dtype=float)
	m, n = A.shape
	U = A.copy()
	L = np.identity(m)
	for k in range(m):
		for i in range(k+1, m):
			L[i,k] = U[i,k] / U[k,k]
			for j in range(k, n):
				 U[i,j] = U[i,j] - L[i,k] * U[k,j]

	return (L, U)
		

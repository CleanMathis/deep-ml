import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	"""
	Perform QR decomposition using Gram-Schmidt process.
	
	Args:
		A: An m x n matrix represented as list of lists
	
	Returns:
		Tuple of (Q, R) where Q is orthogonal and R is upper triangular
	"""
	# Your code here nested loop, i und j Grammer schmidt verfahren relativ leicht, musst nur die Berechnungen mahcen und auf die Struktur achten, erst skalar, dann noch skalar umgedrecht mit aktuellem column, dann column aktuell mit den anderen jeweils um eine Reihe abzudeckem
	A = np.array(A, dtype=float)
	m, n = A.shape
	Q = np.zeros((m, n))
	R = np.zeros((m, n))
	
	for j in range(n):
		v = 0
		for i in range(j):

			dot = 0.0

			for k in range(m):
				dot += Q[k, i] * A[k, j]
			R[i, j] = dot

			for k in range(m):
				A[k, j] -= R[i, j] * Q[k, i]
		
		norm = 0.0
		for k in range(m):
			norm += A[k, j]**2
		R[j, j] = np.sqrt(norm)

		for k in range(m):
			Q[k, j] = A[k, j]/ R[j, j]
	
	return Q, R
			
			
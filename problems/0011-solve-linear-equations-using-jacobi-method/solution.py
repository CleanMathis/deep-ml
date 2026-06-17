import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = [0] * len(b)

	k = 0

	while k < n:
		res = []
		for i in range(len(b)):
			wert = 0
			for j in range(len(A[0])):
				if i != j:
					wert += (A[i][j] * x[j])
			res.append((b[i] - wert)/A[i][i])
		x = res
		k +=1
				
	return x
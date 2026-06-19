import numpy as np

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	c = []
	count = 0
	mg = []
	for i in range(len(matrix)):
		res = []
		mgc = []
		for y in range(len(matrix[0])):
			count += 1  
			m = np.delete(matrix, i, axis=0)
			m = np.delete(m, y, axis=1)
			m_det = np.linalg.det(m)
			if count %2 == 0:
				g = (matrix[i][y] * m_det) * -1
				res.append(g)
			else:
				g = matrix[i][y] * m_det
				res.append(g)
			mgc.append(m_det)
		mg.append(mgc)
		c.append(res)
	
	det = 0
	for i in range(len(c[0])):
		if i%2== 0:
			det += matrix[0][i] * mg[0][i]
		else:
			det += matrix[0][i] * mg[0][i] * -1
	return det


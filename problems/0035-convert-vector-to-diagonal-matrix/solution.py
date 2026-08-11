import numpy as np

def make_diagonal(x):
	#np.diag(x)
	shape = np.size(x)
	matrix = np.zeros((shape, shape))
	for i in range(shape):
		matrix[i][i] = x[i]
	return matrix
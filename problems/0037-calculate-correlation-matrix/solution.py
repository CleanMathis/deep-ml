import numpy as np

def calculate_correlation_matrix(X, Y=None):
	
	cov = np.cov(X, Y, rowvar=False)
	std = np.sqrt(np.diag(cov))
	std_matrix = np.outer(std, std)
	corr = cov/std_matrix
	if Y is None:
		return corr
	return corr[:X.shape[1], X.shape[1]:]
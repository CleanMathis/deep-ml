import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	try:
		t_inv = np.linalg.inv(T)
		w = np.linalg.inv(S)
	except np.linalg.LinAlgError:
		return -1
	
	transformed = np.dot(t_inv, A)
	transformed_matrix = np.dot(transformed, S)

	return transformed_matrix
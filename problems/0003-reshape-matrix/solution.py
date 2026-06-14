import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	reshaped_matrix = []
	res = []
	x = 0
	y = 0
	b = len(a) * len(a[0])

	if b != (new_shape[0] * new_shape[1]):
		return reshaped_matrix
	for i in range(b):
		if y == len(a[0]):
			y = 0
			x+=1

		if len(res) == new_shape[1]:
			reshaped_matrix.append(res)
			res = []
			res.append(a[x][y])
			y+=1
		else:
			res.append(a[x][y])
			y+=1

	reshaped_matrix.append(res)
		
	return reshaped_matrix
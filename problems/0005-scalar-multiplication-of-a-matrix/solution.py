def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = []
	for i in range(len(matrix)):
		res = []
		for y in range(len(matrix[0])):
			res.append(matrix[i][y]*scalar)
		result.append(res)
	
	return result
	
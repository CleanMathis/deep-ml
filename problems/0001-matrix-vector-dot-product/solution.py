def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1

	result = []

	for i in range(len(a)):
		res = 0
		for y in range(len(b)):
			res += a[i][y] * b[y]
		result.append(res)
	return result
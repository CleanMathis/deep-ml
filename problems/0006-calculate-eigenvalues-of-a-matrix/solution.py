def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	mean = (matrix[1][1] + matrix[0][0])/2
	product = (matrix[1][1] * matrix[0][0]) - (matrix[0][1] * matrix[1][0])
	a = mean + (mean**2 - product)**0.5
	b = mean - (mean**2 - product)**0.5

	return [a, b]
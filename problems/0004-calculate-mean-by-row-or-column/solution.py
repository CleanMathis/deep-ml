def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	len_column = len(matrix[0])
	len_row = len(matrix)

	if mode == 'column':
		for x in range(len_column):
			mean = 0
			sume = 0
			for y in range(len_row):
				sume += matrix[y][x]
			mean = sume/len_row
			means.append(mean)
	else:	
		for x in range(len_row):
			mean = 0
			sume = 0
			for y in range(len_column):
				sume += matrix[x][y]
			mean = sume/len_column
			means.append(mean)
	return means
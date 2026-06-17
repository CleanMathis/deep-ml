def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

	means = []

	for i in range(len(vectors)):
		means.append(sum(vectors[i])/len(vectors[i]))

    vector = len(vectors[0])
    c = []
    for i in range(len(vectors)):
        res = []
        for j in range(len(vectors)):
            wert = 0
            for k in range(vector):
				if i == j:
					wert += (vectors[i][k] - means[i]) **2
				else:
                	wert += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
            res.append(wert/(len(vectors[0])-1))
        c.append(res)

	return c
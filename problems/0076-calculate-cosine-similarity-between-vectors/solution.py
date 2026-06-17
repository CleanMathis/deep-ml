import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	if len(v1) == 0 or len(v2) == 0:
		return -1
	skalar = 0
	len_v1 = 0
	len_v2 = 0
	for i in range(len(v1)):
		skalar += v1[i] * v2[i]
		len_v1 += v1[i] **2
		len_v2 += v2[i] **2
	len_v1 = len_v1**0.5
	len_v2 = len_v2**0.5
	if len_v1 == 0 or len_v2 == 0:
		return -1

	return skalar / (len_v1 * len_v2)
	


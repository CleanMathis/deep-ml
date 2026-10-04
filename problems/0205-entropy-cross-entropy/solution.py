import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
	"""
	Compute entropy of P and cross-entropy between P and Q.
	
	Args:
		P: True probability distribution
		Q: Predicted probability distribution
	
	Returns:
		Tuple of (entropy H(P), cross-entropy H(P,Q))
	"""
	if sum(P) != 1 or sum(Q) != 1:
		return -1

	entropy = 0
	cross_entropy = 0
	epsilon = 1e-10

	for i in range(len(P)):
		if P[i] == 0:
			continue
		entropy += P[i]*np.log(P[i])
		if Q[i] == 0:
			cross_entropy += P[i]*np.log(Q[i]+ epsilon)
		else:
			cross_entropy += P[i]*np.log(Q[i])
	entropy *= -1
	cross_entropy *= -1
	return(entropy, cross_entropy)

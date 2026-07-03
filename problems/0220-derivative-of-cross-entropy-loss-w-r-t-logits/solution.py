import math

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	# Schleife 1: Summe aller e^z_i berechnen
	sum_e = 0
	for i in range(len(logits)):
		sum_e += math.exp(logits[i])

	# Schleife 2: Softmax-Wahrscheinlichkeiten berechnen
	prob_logit = []
	for i in range(len(logits)):
		prob_logit.append(math.exp(logits[i]) / sum_e)

	prob_logit[target] = prob_logit[target] - 1
	return prob_logit
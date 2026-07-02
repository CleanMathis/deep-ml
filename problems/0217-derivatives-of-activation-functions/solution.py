import math

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	sigmoid = (1 / (1 + math.exp(-x))) * (1- (1 / (1 + math.exp(-x))))
	tanh = 1- math.tanh(x)**2
	relu = 0.0
	if x > 0:
		relu = 1.0
	return {'sigmoid': sigmoid,'tanh': tanh, 'relu': relu}
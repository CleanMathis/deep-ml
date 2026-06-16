import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	alle_gleich = all(element == 0 for element in gradient) if gradient else True
	if alle_gleich == True:
		return {'magnitude': 0, 'direction': gradient, 'descent_direction': gradient}
	direction = []
	descent_direction = []
	summe = 0
	for i in range(len(gradient)):
		summe += gradient[i]**2

	magnitude = summe**0.5

	for i in range(len(gradient)):
		direction.append(gradient[i]/magnitude)
		descent_direction.append(gradient[i]/magnitude * -1)
	
	return {'magnitude' : magnitude, 'direction': direction, 'descent_direction': descent_direction}

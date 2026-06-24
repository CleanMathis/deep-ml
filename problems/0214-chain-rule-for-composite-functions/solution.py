import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
    res = 1
    x = x
	for i in range(len(functions)-1, -1, -1):
        if functions[i] == 'square':
            res *= 2*x
            x = x**2
        elif functions[i] == 'sin':
            res *= np.cos(x)
            x = np.sin(x)
        elif functions[i] == 'exp':
            res *= np.exp(x)
            x = np.exp(x)
        elif functions[i] == 'log':
            res *= 1/x
            x = np.log(x)
        else:
            raise ValueError(f'Invalid function: {functions[i]}')
	return res

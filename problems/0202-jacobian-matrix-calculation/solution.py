import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
    x = np.array(x, dtype=float)
    f0 = np.array(f(x))
    m = len(f0)
    n = len(x)

    J = np.zeros((m, n))

    for j in range(n):
        x_shifted = x.copy()
        x_shifted[j] += h
        f_shifted = np.array(f(x_shifted))
        J[:, j] = (f_shifted - f0) / h

    return J.tolist()
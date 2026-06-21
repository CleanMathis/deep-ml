import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	theta = np.linalg.lstsq(X, y)
	return theta[0]
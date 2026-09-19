import numpy as np

def classify_critical_point(hessian: np.ndarray, tol: float = 1e-10):
    eigenvalues, eigenvector = np.linalg.eig(hessian)
    if np.all(eigenvalues > tol):
        return -1
    elif np.all(eigenvalues < -tol):
        return 1
    elif np.any(eigenvalues > tol) and np.any(eigenvalues < -tol):
        return 0
    else:
        return None
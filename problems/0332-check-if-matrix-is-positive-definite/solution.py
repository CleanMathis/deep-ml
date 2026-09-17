import numpy as np

def check_positive_definite(matrix: list) -> dict:
    """
    Check if a matrix is positive definite and compute its eigenvalues.
    
    Args:
        matrix: A 2D list representing a square matrix
        
    Returns:
        dict with 'is_positive_definite' (bool) and 'eigenvalues' (list of floats sorted ascending)
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)


    count = 0
    is_positive_definite = bool(np.all(eigenvalues > 0))
    
    
    eigenvalues.sort()
    for i in range(len(eigenvalues)):
        eigenvalues[i] = round(eigenvalues[i], 4)
    
    return {'is_positive_definite': is_positive_definite, 'eigenvalues': eigenvalues.tolist()}

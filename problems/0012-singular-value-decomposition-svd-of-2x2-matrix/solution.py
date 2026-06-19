import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    a_t = np.transpose(A)
    M = np.dot(a_t, A)
    trace = M[0][0] + M[1][1]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    x1 = np.sqrt((trace + np.sqrt(trace ** 2 - 4 * det)) / 2) # Mitternachtformel = quadratische Formel x werte bestimmen (-b +- sqrt(b^2 - 4ac)) / 2a
    x2 = np.sqrt((trace - np.sqrt(trace ** 2 - 4 * det)) / 2)
    S = [x1, x2]
    S_diagonal = np.diag(S)
    v1 = [M[0][1],x1**2 - M[0][0] ]
    v2 = [x2**2 - M[1][1], M[1][0]]
    v1_n = np.linalg.norm(v1)
    v2_n = np.linalg.norm(v2)
    v1_norm = v1/v1_n
    v2_norm = v2/v2_n
    V = np.array([v1_norm, v2_norm])
    g = np.dot(A, np.transpose(V))
    U = np.dot(g, np.linalg.inv(S_diagonal))

    return U, S, V
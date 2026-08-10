import numpy as np

def pairwise_cosine_similarity(X):
    X = np.array(X)
    norm = np.linalg.norm(X, axis=1, keepdims=True)
    X_normalized = X / norm
    np.nan_to_num(X_normalized, 0)
    return X_normalized @ X_normalized.T
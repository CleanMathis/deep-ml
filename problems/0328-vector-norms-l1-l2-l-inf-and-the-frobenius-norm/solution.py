import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    if norm_type == 'l1':
        norm = 0
        for element in arr.flatten():
            norm += abs(element)
        return norm
    elif norm_type == 'l2' or norm_type == 'frobenius':
        norm = 0
        for element in arr.flatten():
            norm += element ** 2
        return np.sqrt(norm)
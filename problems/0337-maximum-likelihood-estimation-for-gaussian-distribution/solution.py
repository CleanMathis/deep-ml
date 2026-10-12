import numpy as np

def gaussian_mle(data: np.ndarray) -> tuple:
    """
    Compute Maximum Likelihood Estimates for Gaussian distribution parameters.
    
    Args:
        data: 1D numpy array of observations
        
    Returns:
        Tuple of (mean_mle, variance_mle)
    """
    mean_mle = sum(data)/data.size
    variance_mle = 0

    for i in range(data.size):
        variance_mle += (data[i] - mean_mle)**2
    variance_mle = variance_mle / data.size
    return (mean_mle, variance_mle)
import numpy as np

def multivariate_kl_divergence(mu_p: np.ndarray, Cov_p: np.ndarray, mu_q: np.ndarray, Cov_q: np.ndarray) -> float:
    """
    Computes the KL divergence between two multivariate Gaussian distributions.
    
    Parameters:
    mu_p: mean vector of the first distribution
    Cov_p: covariance matrix of the first distribution
    mu_q: mean vector of the second distribution
    Cov_q: covariance matrix of the second distribution

    Returns:
    KL divergence as a float
    """
    inv_Covq = np.linalg.inv(Cov_q)
    log = np.log((np.linalg.det(Cov_q)/np.linalg.det(Cov_p)))
    dim = len(mu_p)
    trans = np.transpose((mu_p - mu_q))
    doter = np.dot(trans, inv_Covq)
    mu_cluster = np.dot(doter, (mu_p - mu_q))
    dot = np.dot(inv_Covq, Cov_p)
    inve = np.trace(dot)
    return 1/2 * (log - dim + mu_cluster + inve)
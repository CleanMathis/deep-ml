import math

def softmax_derivative(x: list[float]) -> list[list[float]]:
    """
    Compute the Jacobian matrix of the softmax function.
    
    Args:
        x: Input vector of real numbers
        
    Returns:
        Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
    """
    softmax = []
    sum_e = 0
    for i in range(len(x)):
        sum_e += math.exp(x[i])
    softmax = [math.exp(xi) / sum_e for xi in x]

    jacobi = []
    for i in range(len(softmax)):
        row = []
        for j in range(len(softmax)):
            if i == j:
                row.append(softmax[i] * (1 - softmax[i]))
            else:
                row.append(-softmax[i] * softmax[j])
        jacobi.append(row)
    return jacobi


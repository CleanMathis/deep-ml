import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    if len(g_coeffs) >= len(h_coeffs):
        bed = len(g_coeffs)
    else:
        bed = len(h_coeffs)

    g_coeffs = g_coeffs[::-1]
    h_coeffs = h_coeffs[::-1]
    g1_coeffs = [0] *(len(g_coeffs)-1)
    h1_coeffs = [0] *(len(h_coeffs)-1)

    for i in range(1, len(g_coeffs)):
        g1_coeffs[i-1] = g_coeffs[i] * i

    for i in range(1, len(h_coeffs)):
        h1_coeffs[i-1] = h_coeffs[i] * i

    if len(g1_coeffs) == 0:
        g1 = 0
    else:
        g1 = g1_coeffs[0]

    if len(h1_coeffs) == 0:
        h1 = 0
    else:
        h1 = h1_coeffs[0]
    
    g = g_coeffs[0]
    h = h_coeffs[0]
    
    i = 1

    while i < bed:
        if i < len(g_coeffs):
            g += g_coeffs[i] * x **i
        if i < len(g1_coeffs):
            g1 += g1_coeffs[i] * x **i
        if i < len(h_coeffs):
            h += h_coeffs[i] * x **i
        if i < len(h1_coeffs):
            h1 += h1_coeffs[i] * x **i
        i +=1

    res = (g1*h - g*h1)/h**2


    return res
import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
    if x_ini is None:
        x_ini = np.zeros(b.shape)
    DL = np.tril(A)
    U = np.triu(A, k=1)
    for i in range(n):
        rhs = b-  U@x_ini
        x_neu = np.linalg.solve(DL, rhs)
        x_ini = x_neu
    return x_ini
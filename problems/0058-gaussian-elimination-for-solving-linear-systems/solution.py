import numpy as np

def gaussian_elimination(A, b):
    # Datentypen für genaue Fließkomma-Rechnung sicherstellen
    A = A.astype(float)
    b = b.astype(float)
    n = len(A)

    # 1. Vorwärtselimination (mit partiellem Pivoting)
    for i in range(n - 1):
        # Partielles Pivoting: Zeile mit größtem Betrag in Spalte i finden
        max_index = i + np.argmax(np.abs(A[i:, i]))
        if max_index != i:
            A[[i, max_index]] = A[[max_index, i]]
            b[[i, max_index]] = b[[max_index, i]]

        # Elimination für alle Zeilen darunter
        for k in range(i + 1, n):
            m = A[k, i] / A[i, i]
            A[k] = A[k] - m * A[i]
            b[k] = b[k] - m * b[i]

    # 2. Rückwärtssubstitution
    x = np.zeros(n)
    for j in range(n - 1, -1, -1):
        x[j] = (b[j] - np.dot(A[j, j + 1:], x[j + 1:])) / A[j, j]

    return x
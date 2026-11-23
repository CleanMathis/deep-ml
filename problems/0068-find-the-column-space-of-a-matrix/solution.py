
import numpy as np

def matrix_image(A):
    rank = np.linalg.matrix_rank(A)
    if rank == 0:
        return None
    m = np.array(A, dtype=float)
    tol = 1e-10 
    rows, columns = A.shape
    pivot = 0
    pivot_col = []
    for col in range(columns):
        if pivot == rank:
            break
        found = False

        for row in range(pivot, rows):
            if found:
                break
            if m[row][col] > tol or -tol > m[row][col]:
                found = True
                found_row = row
                
        if found and pivot != found_row:
            m[[pivot, found_row]] = m[[found_row, pivot]]
            
        if found:
            faktor = 1/m[pivot][col]
            m[pivot] = m[pivot] *faktor
            for x in range(pivot+1, rows):
                faktor_row = m[x][col]
                m[x] = m[x] - m[pivot]*faktor_row
            pivot +=1
            pivot_col.append(col)
            
    return A[:,pivot_col]
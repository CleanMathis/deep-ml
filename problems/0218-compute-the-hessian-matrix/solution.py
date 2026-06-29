from typing import Callable

def compute_hessian(
    f: Callable[[list[float]], float],
    point: list[float],
    h: float = 1e-5
) -> list[list[float]]:
    
    n = len(point)
    hessian = [[0.0 for _ in range(n)] for _ in range(n)]

    def shift(vec, i, delta):
        new_vec = vec.copy()
        new_vec[i] += delta
        return new_vec

    for i in range(n):
        for j in range(n):
            if i == j:
                forward = f(shift(point, i, h))
                backward = f(shift(point, i, -h))
                center = f(point)
                
                hessian[i][j] = (forward - 2 * center + backward) / (h ** 2)
            else:
                pp = f(shift(shift(point, i, h), j, h))
                pm = f(shift(shift(point, i, h), j, -h))
                mp = f(shift(shift(point, i, -h), j, h))
                mm = f(shift(shift(point, i, -h), j, -h))
                
                hessian[i][j] = (pp - pm - mp + mm) / (4 * h ** 2)

    return hessian
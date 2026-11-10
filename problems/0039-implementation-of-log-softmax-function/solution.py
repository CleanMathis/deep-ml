import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    softmax = []
    summe = 0
    maxe = max(scores)
    for i in scores:
        summe += np.exp(i - maxe)
    log_summe = np.log(summe)
    for i in range(len(scores)):
        x = scores[i] -maxe - log_summe
        softmax.append(x)
    return softmax
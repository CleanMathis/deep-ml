import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n = np.shape(data)
    rand = np.random.default_rng(seed).permutation(n[0])

    train_end = int(n[0] * train_frac)
    validation_end = train_end + int(n[0] * validation_frac)
    train = data[rand[: train_end]]
    val = data[rand[train_end: validation_end]]
    test = data[rand[validation_end:]]

    return [train, val , test]
import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """


    mean               = np.mean(data)
    median             = np.median(data)
    count = 0
    current = 1
    mode = data[0]

    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            current +=1
        else:
            if current > count:
                mode = data[i-1]
                count = current
            current = 1
    if current > count:
        mode = data[len(data)-2]

    variance           = np.var(data)
    standard_deviation = np.std(data)
    p25                = np.percentile(data, 25)
    p50                = np.percentile(data, 50)
    p75                = np.percentile(data, 75)
    interquartile_range = p75 - p25

    return {
    "mean": float(mean),
    "median": float(median),
    "mode": int(mode),
    "variance": float(variance),
    "standard_deviation": float(standard_deviation),
    "25th_percentile": float(p25),
    "50th_percentile": float(p50),
    "75th_percentile": float(p75),
    "interquartile_range": float(interquartile_range)
    }


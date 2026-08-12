def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    x = len(samples)
    samples.sort()
    seen = []
    count = 0
    res = []
    if x == 0:
        return []
    previous = samples[0]
    
    for sample in samples:
        if sample not in seen:
            seen.append(sample)
        
        if previous == sample:
            count +=1
        else:
            res.append((previous, count/x))
            count = 1
            previous = sample
    res.append((previous, count/x))
    return res

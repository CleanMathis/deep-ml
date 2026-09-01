def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    xy_count = 0
    x_count = 0
    for i in range(len(data)):
      if data[i][0] == x and data[i][1] == y:
        x_count +=1
        xy_count +=1
      elif data[i][0] == x:
        x_count +=1
    if x_count == 0:
      return 0
    return xy_count/x_count
        
      
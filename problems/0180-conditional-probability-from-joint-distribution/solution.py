def conditional_probability(joint_distribution: dict) -> float:
	"""
	Compute conditional probability P(A|B) from a joint probability distribution.

	Args:
		joint_distribution (dict): dictionary with keys ('A','B'), ('A','`B'), ('`A','B'), ('`A','`B')

	Returns:
		float: Conditional probability P(A|B)
	"""
	bres = 0
	div = 0
	for key, value in joint_distribution.items():
		if key[1] == 'B':
			bres += value
			if key[0] == 'A':
				div = value
	return div/bres

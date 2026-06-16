import numpy as np

def accuracy_score(y_true, y_pred):
	count = 0
	for i in range(len(y_true)):
		if y_true[i] == y_pred[i]:
			count +=1
	
	return count / len(y_true)
	
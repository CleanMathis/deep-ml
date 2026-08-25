import numpy as np

def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-z))
	
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    weights = initial_weights.copy()
    bias = initial_bias
    mse_values = []
    
    n = len(labels)
    
    for _ in range(epochs):
        # 1. Forward Pass
        z = np.dot(features, weights) + bias
        predictions = sigmoid(z)
        
        # 2. Loss Calculation (MSE)
        mse = np.mean((predictions - labels) ** 2)
        mse_values.append(np.round(float(mse), 4))
        
        # 3. Gradient Calculation (Backward Pass)
        # derivative of sigmoid: σ'(z) = σ(z) * (1 - σ(z))
        sigmoid_derivative = predictions * (1 - predictions)
        error = predictions - labels
        
        # Combined delta term: 2/n * (σ(z) - y) * σ'(z)
        delta = (2 / n) * error * sigmoid_derivative
        
        dw = np.dot(features.T, delta)
        db = np.sum(delta)
        
        # 4. Parameter Update
        weights -= learning_rate * dw
        bias -= learning_rate * db
        
    return np.round(weights, 4), np.round(bias, 4), mse_values
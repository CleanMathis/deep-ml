import torch

def to_float_tensor(values):
    x_values = torch.tensor(values, dtype=torch.float32)
    return x_values

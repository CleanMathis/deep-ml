import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    result = data.copy()
    n_rows, n_cols = result.shape

    for col in range(n_cols):
        # Fehlende Stellen finden
        missing_positions = []
        valid_values = []

        for row in range(n_rows):
            if np.isnan(result[row, col]):
                missing_positions.append(row)
            else:
                valid_values.append(result[row, col])

        # Ersatzwert je nach Strategie berechnen
        if len(missing_positions) == 0 or len(valid_values) == 0:
            continue

        if strategy == 'mean':
            fill_value = sum(valid_values) / len(valid_values)
        elif strategy == 'median':
            sorted_vals = sorted(valid_values)
            n = len(sorted_vals)
            if n % 2 == 1:
                fill_value = sorted_vals[n // 2]
            else:
                fill_value = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
        elif strategy == 'mode':
            # Häufigster Wert
            counts = {}
            for v in valid_values:
                counts[v] = counts.get(v, 0) + 1
            fill_value = max(counts, key=counts.get)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        # Fehlende Stellen auffüllen
        for row in missing_positions:
            result[row, col] = fill_value

    return result


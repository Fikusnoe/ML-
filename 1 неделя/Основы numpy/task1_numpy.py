import numpy as np

def sum_prod(X, V):
    if len(X) == 0:
        return np.array([])

    X_arr = np.array(X)
    V_arr = np.array(V)

    result = np.sum(X_arr @ V_arr, axis=0)

    return result
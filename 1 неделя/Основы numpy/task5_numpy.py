import numpy as np

def chess(m, n, a, b):
    i_indices, j_indices = np.ogrid[:m, :n]
    chess_pattern = (i_indices + j_indices) % 2

    result = np.where(chess_pattern == 0, a, b)
    return result
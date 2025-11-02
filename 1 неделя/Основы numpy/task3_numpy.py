import numpy as np

def get_unique_rows(matrix):
    if matrix.ndim != 2:
        return "Матрица должна быть двумерной"
    result = []
    for i in range(matrix.shape[0]):
        unique_elements = np.unique(matrix[i, :])
        result.append(unique_elements)
    return result


def get_unique_columns(matrix):
    if matrix.ndim != 2:
        return "Матрица должна быть двумерной"
    result = []
    for j in range(matrix.shape[1]):
        unique_elements = np.unique(matrix[:, j])
        result.append(unique_elements)

    return result
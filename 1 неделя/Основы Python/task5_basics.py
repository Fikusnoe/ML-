def mse(pred, true):
    if len(pred) != len(true):
        return  "Векторы должны быть одинаковой длины"

    if len(pred) == 0:
        return 0

    squared_errors = [(p - t) ** 2 for p, t in zip(pred, true)]
    return sum(squared_errors) / len(squared_errors)
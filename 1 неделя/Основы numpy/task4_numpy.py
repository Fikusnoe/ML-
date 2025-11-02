import numpy as np
import matplotlib.pyplot as plt

def analyze_normal_matrix(m, n, mean=0, std=1):
    matrix = np.random.normal(loc=mean, scale=std, size=(m, n))

    print(f"Матрица {m}x{n}:")
    print(matrix)

    # Статистика по столбцам
    column_means = np.mean(matrix, axis=0)
    column_variances = np.var(matrix, axis=0)

    print("Статистика по СТОЛБЦАМ:")
    for i in range(n):
        print(f"Столбец {i + 1}: мат. ожидание = {column_means[i]:.4f}, "
              f"дисперсия = {column_variances[i]:.4f}")

    row_means = np.mean(matrix, axis=1)
    row_variances = np.var(matrix, axis=1)

    print("Статистика по СТРОКАМ:")
    for i in range(m):
        print(f"Строка {i + 1}: мат. ожидание = {row_means[i]:.4f}, "f"дисперсия = {row_variances[i]:.4f}")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].set_title("Гистограммы значений по СТРОКАМ")
    for i in range(m):
        axes[0, 0].hist(matrix[i, :], alpha=0.7, label=f"Строка {i + 1}",
                        bins=15, density=True)
    axes[0, 0].legend()
    axes[0, 0].set_xlabel("Значения")
    axes[0, 0].set_ylabel("Плотность")
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].set_title("Гистограммы значений по СТОЛБЦАМ")
    for j in range(n):
        axes[0, 1].hist(matrix[:, j], alpha=0.7, label=f"Столбец {j + 1}", bins=15, density=True)
    axes[0, 1].legend()
    axes[0, 1].set_xlabel("Значения")
    axes[0, 1].set_ylabel("Плотность")
    axes[0, 1].grid(True, alpha=0.3)

    axes[1, 0].hist(matrix.flatten(), bins=20, alpha=0.7, density=True)
    axes[1, 0].set_title("Гистограмма всех значений матрицы")
    axes[1, 0].set_xlabel("Значения")
    axes[1, 0].set_ylabel("Плотность")
    axes[1, 0].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return matrix, column_means, column_variances, row_means, row_variances

analyze_normal_matrix(3, 4, mean=2, std=0.5)
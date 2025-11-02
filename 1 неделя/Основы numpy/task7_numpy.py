import numpy as np
import matplotlib.pyplot as plt

def analyze_time_series(series, window_size):
    mean = np.mean(series)
    variance = np.var(series)
    std = np.std(series)
    local_maxima = []
    local_minima = []
    
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            local_maxima.append((i, series[i]))
        if series[i] < series[i-1] and series[i] < series[i+1]:
            local_minima.append((i, series[i]))
    
    moving_average = np.convolve(series, np.ones(window_size)/window_size, mode='valid')
    
    return {
        'mean': mean,
        'variance': variance,
        'std': std,
        'local_maxima': local_maxima,
        'local_minima': local_minima,
        'moving_average': moving_average
    }


np.random.seed(42)
t = np.linspace(0, 4*np.pi, 50)
test_series = np.sin(t) + 0.2 * np.random.normal(size=len(t))
window_size = 3
results = analyze_time_series(test_series, window_size)

print("Результаты:")
print(f"Среднее: {results['mean']:.3f}")
print(f"Дисперсия: {results['variance']:.3f}")
print(f"СКО: {results['std']:.3f}")
print(f"Локальных максимумов: {len(results['local_maxima'])}")
print(f"Локальных минимумов: {len(results['local_minima'])}")
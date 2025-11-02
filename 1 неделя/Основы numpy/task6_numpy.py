import numpy as np
import matplotlib.pyplot as plt

def draw_rectangle(a, b, m, n, rectangle_color, background_color):
    image = np.full((n, m, 3), background_color, dtype=np.uint8)
    x_start = (m - a) // 2
    y_start = (n - b) // 2
    x_end = x_start + a
    y_end = y_start + b  
    image[y_start:y_end, x_start:x_end] = rectangle_color
    return image

def draw_ellipse(a, b, m, n, ellipse_color, background_color):
    image = np.full((n, m, 3), background_color, dtype=np.uint8)
    x0, y0 = m // 2, n // 2
    x = np.arange(m)
    y = np.arange(n)
    X, Y = np.meshgrid(x, y)
    ellipse_mask = ((X - x0) / a)**2 + ((Y - y0) / b)**2 <= 1
    image[ellipse_mask] = ellipse_color
    return image
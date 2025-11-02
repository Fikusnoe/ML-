import numpy as np
import matplotlib.pyplot as plt

def one_hot_encoding(labels):
    num_classes = np.max(labels) + 1
    encoding = np.zeros((len(labels), num_classes), dtype=int)
    encoding[np.arange(len(labels)), labels] = 1
    return encoding
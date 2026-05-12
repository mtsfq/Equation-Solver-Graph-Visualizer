# هذا الملف لاكواد رسم الدالات

import matplotlib.pyplot as plt
import numpy as np

def plot_function(func):
    x = np.linspace(-10, 10, 100)
    y = func(x)

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.plot(x, y)
    plt.show()

plot_function(lambda x: x**2 + 3*x + 2)
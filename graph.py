# هذا الملف لاكواد رسم الدالات


import matplotlib.pyplot as plt
import numpy as np

def plot_graph(func):
    x_vals = np.linspace(-10, 10, 400)
    # محاولة حساب قيم y، وإذا كانت الدالة ثابتة (مثل رقم 5) نحولها لمصفوفة
    try:
        y_vals = func(x_vals)
    except:
        y_vals = np.full_like(x_vals, func)
        
    plt.plot(x_vals, y_vals)
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.grid(True)
    plt.title("Graph Visualization")
    plt.show()
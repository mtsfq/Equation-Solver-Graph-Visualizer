# هذا الملف لاكواد رسم الدالات


import numpy as np
import matplotlib.pyplot as plt

from sympy import symbols, lambdify

from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)

x = symbols('x')

transformations = (
    standard_transformations +
    (implicit_multiplication_application,)
)


def plot_graph(expression):

    expression = expression.replace(
        "^",
        "**"
    )

    expr = parse_expr(
        expression,
        transformations=transformations
    )

    function = lambdify(
        x,
        expr,
        "numpy"
    )

    x_values = np.linspace(
        -10,
        10,
        500
    )

    y_values = function(
        x_values
    )

    plt.figure(
        figsize=(8,6)
    )

    plt.plot(
        x_values,
        y_values,
        label=expression
    )

    plt.axhline(
        y=0
    )

    plt.axvline(
        x=0
    )

    plt.grid(True)

    plt.legend()

    plt.title(
        "Graph"
    )

    plt.xlabel("x")

    plt.ylabel("y")

    plt.show(block=False)
# هذا الملف يحتوي على دوال حساب الاشتقاق والتكامل


from sympy import *

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


def derivative(expression):

    expression = expression.replace(
        "^",
        "**"
    )

    expr = parse_expr(
        expression,
        transformations=transformations
    )

    result = diff(
        expr,
        x
    )

    return result



def integral(expression):

    expression = expression.replace(
        "^",
        "**"
    )

    expr = parse_expr(
        expression,
        transformations=transformations
    )

    result = integrate(
        expr,
        x
    )

    return result
# هذا الملف يحتوي على الكود الخاص بحل المعادلات الرياضية باستخدام مكتبة sympy


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


def solve_equation(expression):

    try:

        expression = expression.replace("^","**")

        if "=" in expression:

            left,right = expression.split("=")

            equation = Eq(

                parse_expr(
                    left,
                    transformations=transformations
                ),

                parse_expr(
                    right,
                    transformations=transformations
                )
            )

            solution = solve(
                equation,
                x
            )

            return solution

        else:

            expr = parse_expr(
                expression,
                transformations=transformations
            )

            solution = solve(
                expr,
                x
            )

            return solution

    except Exception as e:

        return str(e)
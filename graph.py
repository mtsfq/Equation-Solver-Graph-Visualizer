# هذا الملف لاكواد رسم الدالات


import numpy as np
import matplotlib.pyplot as plt

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
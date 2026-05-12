# هذا الملف الاساسي

# from sympy import *
# from sympy.parsing.sympy_parser import parse_expr

# x = symbols('x')

# user_input = input("Enter math expression: ")

# try:

#     # إذا فيها =
#     if "=" in user_input:

#         left, right = user_input.split("=")

#         equation = Eq(parse_expr(left), parse_expr(right))

#         solution = solve(equation, x)

#         print("Solution:")
#         print(solution)

#     # إذا فيها integrate
#     elif "integrate" in user_input.lower():

#         expression = user_input.replace("integrate", "")

#         result = integrate(parse_expr(expression), x)

#         print("Integral:")
#         print(result)

#     # إذا فيها derivative
#     elif "derivative" in user_input.lower():

#         expression = user_input.replace("derivative", "")

#         result = diff(parse_expr(expression), x)

#         print("Derivative:")
#         print(result)

#     else:

#         print("Unknown expression")

# except Exception as e:

#     print("Error:")
#     print(e)



from sympy import symbols, Eq, solve, diff, integrate, sympify
from sympy.parsing.sympy_parser import parse_expr
from graph import plot_graph

x = symbols('x')

user_input = input("Enter math expression: ")

try:
    # حل المعادلات
    if "=" in user_input:
        left, right = user_input.split("=")
        equation = Eq(parse_expr(left), parse_expr(right))
        solution = solve(equation, x)

        print("Solution:")
        print(solution)

    # الاشتقاق
    elif "derivative" in user_input.lower():
        expression = user_input.lower().replace("derivative", "").strip()
        result = diff(parse_expr(expression), x)

        print("Derivative:")
        print(result)

    # التكامل
    elif "integrate" in user_input.lower():
        expression = user_input.lower().replace("integrate", "").strip()
        result = integrate(parse_expr(expression), x)

        print("Integral:")
        print(result)

    # الرسم البياني
    else:
        expression = parse_expr(user_input)
        print("Drawing graph...")
        plot_graph(expression)

except Exception as e:
    print("Error:")
    print(e)
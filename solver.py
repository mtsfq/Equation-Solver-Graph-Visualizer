# هذا الكود يستخدم مكتبة sympy لحل المعادلات الجبرية.


from sympy import symbols, solve

# تعريف المتغير x
x = symbols('x')

# دالة حل المعادلات
def solve_equation(expression):
    solutions = solve(expression, x)
    return solutions


# اختبار
equation = x**2 + 3*x + 2

result = solve_equation(equation)

print("Solutions:")
print(result)
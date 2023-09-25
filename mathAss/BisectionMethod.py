import sympy as sp


def bisection_method(func, a, b, tol):
    """
    Compute an approximate root of the function func within the interval [a, b] using the bisection method.

    :param func: The target function to find the root of.
    :param a: The left endpoint of the interval.
    :param b: The right endpoint of the interval.
    :param tol: The tolerance (desired accuracy) for the root.
    :param max_iter: The maximum number of iterations allowed.
    :return: An approximate root of the function.
    """
    iteration = 0
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        sign_a = func.subs(x, a).evalf()
        sign_midpoint = func.subs(x, midpoint).evalf()

        if sign_a * sign_midpoint < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1
    print(f"number of iteration = {iteration}")
    approximate_root = (a + b) / 2.0
    print(
        f"Therefore the interval of transedental equation lies between [ {approximate_root} , {b}]")
    return approximate_root


# Get user input for the target function
func_str = input(
    "Enter the target function as a valid Python expression (e.g., 'x * exp(x) - 2'): ")

# Define the symbolic variable 'x'
x = sp.symbols('x')

try:
    # Create a SymPy expression from the user input
    target_function = sp.sympify(func_str)
except (sp.SympifyError, ValueError):
    print("Invalid function expression. Please enter a valid mathematical expression.")
    exit()

# Get user input for 'a', 'b', 'tolerance', and 'max_iterations'
a = float(input("Enter the left endpoint 'a': "))
b = float(input("Enter the right endpoint 'b': "))
tolerance = float(input("Enter the tolerance (e.g., 1e-6): "))

# Find the root of the function using the bisection method
root = bisection_method(target_function, a, b, tolerance)

print(f"Approximate root: {root}")

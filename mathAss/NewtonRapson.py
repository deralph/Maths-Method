def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for finding the root of a function.

    Parameters:
    f: function
        The function for which you want to find the root.
    df: function
        The derivative of the function 'f'.
    x0: float
        Initial guess for the root.
    tol: float, optional
        Tolerance (convergence criterion).
    max_iter: int, optional
        Maximum number of iterations.

    Returns:
    x: float
        Approximate root of the function 'f'.
    iterations: int
        Number of iterations required to converge.
    """
    x = x0
    iterations = 0

    while abs(f(x)) > tol and iterations < max_iter:
        x = x - f(x) / df(x)
        iterations += 1

    return x, iterations


# Example usage:
if __name__ == "__main__":
    # Define your function and its derivative
    def f(x):
        return x**2 - 4

    def df(x):
        return 2*x

    # Initial guess
    x0 = 3.0

    # Find the root
    root, iterations = newton_raphson(f, df, x0)

    print(f"Approximate root: {root}")
    print(f"Iterations required: {iterations}")

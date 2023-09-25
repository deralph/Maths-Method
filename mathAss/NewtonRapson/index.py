import sympy as sp

# function to calculate the formula for newton rapson


def formula(f, df, x0):
    soln_f = f.subs(x, x0).evalf()
    soln_df = df.subs(x, x0).evalf()
    result = x0-(soln_f/soln_df)
    return round(result, 5)


def Newton_Rapson(num):

    iteration = 0
    prev_root = None
    initial_x = num
    while iteration < 100:
        iteration += 1
        result = formula(target_f, target_df, initial_x)
        if prev_root == result:
            print(f"The root is {result}")
            break
        else:
            prev_root = result
            initial_x = result
    return iteration


# Get user input for the target function
func_f = input(
    "Enter the target function as a valid Python expression (e.g., 'x * exp(x) - 2'): ")
func_df = input(
    "Enter the target differentiated function as a valid Python expression (e.g., 'x * exp(x) - 2'): ")

# Define the symbolic variable 'x'
x = sp.symbols('x')

try:
    # Create a SymPy expression from the user input
    target_f = sp.sympify(func_f)
    target_df = sp.sympify(func_df)
except (sp.SympifyError, ValueError):
    print("Invalid function expression. Please enter a valid mathematical expression.")
    exit()

# Get user input for x0
x0 = float(input("enter value for x0: "))

root = Newton_Rapson(x0)
print(f"the total amount of iteration is : {root}")

# Bisection Method for Finding Roots

## Description

This Python script uses the bisection method to find an approximate root of a given mathematical function within a specified interval. The bisection method is an iterative numerical technique for solving equations of the form f(x) = 0.

## How to Use

1. **Enter the Target Function Expression**

   When you run the script, you will be prompted to enter the target function as a valid Python expression. For example, you can enter expressions like `x**2 - 4` or `sin(x) + cos(x)`.

2. **Define the Symbolic Variable 'x'**

   The script defines a symbolic variable 'x' using SymPy.

3. **Enter the Interval Endpoints 'a' and 'b'**

   You will be asked to input the left endpoint 'a' and the right endpoint 'b' of the interval in which you want to find the root.

4. **Enter the Tolerance**

   Provide the tolerance (desired accuracy) for the root. A typical value might be `1e-6`.

5. **Run the Bisection Method**

   The script will then execute the bisection method to find an approximate root of the function within the specified interval. It will display the number of iterations performed and the resulting approximate root.

6. **Review the Results**

   The script will output the approximate root found using the bisection method.

## Example

Suppose you want to find the root of the function `x**2 - 4` in the interval [1, 3] with a tolerance of `1e-6`. You would run the script and provide the following inputs:

- Target Function: `x**2 - 4`
- Left Endpoint 'a': `1`
- Right Endpoint 'b': `3`
- Tolerance: `1e-6`

The script will execute and display the number of iterations performed and the approximate root.

## Notes

- Ensure that the target function you provide is a well-formed mathematical expression that SymPy can understand. Invalid expressions will result in an error message.
- The bisection method is an iterative technique that refines the root estimate in each iteration until the desired tolerance is reached. It works well for continuous functions with one root within the specified interval.

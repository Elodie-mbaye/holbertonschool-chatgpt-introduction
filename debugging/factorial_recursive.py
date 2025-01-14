#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer recursively.

    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.
             Must be 0 or a positive integer.

    Returns:
    int: The factorial of the given integer n. 
         If n is 0, returns 1 as 0! = 1 by definition.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive call to calculate factorial

# Main script execution
# Read an integer from command-line arguments, calculate its factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)


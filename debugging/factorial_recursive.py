#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        This function calculates the factorial of a given number using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial will be calculated.

    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)

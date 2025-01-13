#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except (IndexError, ValueError):
        print("Usage: ./factorial.py <non-negative integer>")


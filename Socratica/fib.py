"""
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
    print n, ";", fibonacci(n)
"""
fibonacci_cache = {}

def fibonacci(n):
    # If we have chached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 51):
    print float(fibonacci(n+1)) / fibonacci(n)




"""
from functools import lru_cache # Works in  python 3x

@lru_cache(maxsize = 1000)
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 501):
    print n, ";", fibonacci(n)
"""

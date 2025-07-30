def factorial(n: int) -> int:
    """Calculates the factorial of a number using recursion."""
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1


    return n * factorial(n - 1)


print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1
print(factorial(4))  # Output: 24


def fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number using recursion."""
    
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n > 1:
        return fibonacci(n -1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5
print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(6))  # Output: 8
print(fibonacci(10))  # Output: 55

def sum_recursive(n: int) -> int:
    """Calculates the sum of all integers from 1 to n using recursion."""
    
    if n < 0:
        raise ValueError("Sum is not defined for negative numbers.")
    
    if n == 0:
        return 0
    
    return n + sum_recursive(n - 1)

print(sum_recursive(5))  # Output: 15
print(sum_recursive(0))  # Output: 0
print(sum_recursive(1))  # Output: 1
print(sum_recursive(4))  # Output: 10
print(sum_recursive(10))  # Output: 55
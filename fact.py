# Recursive function to calculate factorial of n
def factorial(n):
    if n == 0 or n == 1:
        # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        # Recursive case: n * factorial(n-1)
        return n * factorial(n - 1)

# Print factorial of 6
print(factorial(6))
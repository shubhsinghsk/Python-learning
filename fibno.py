# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        # Base case: F(0) = 0
        return 0
    elif n == 1:
        # Base case: F(1) = 1
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print the 10th Fibonacci number
print(fibonacci(10))
# Global variable to store the factorial result
fact = 1

# Recursive function to calculate factorial using a global variable
def find_factorial(n):
    global fact
    if n == 0:
        # Base case: when n reaches 0, print the factorial result
        print(fact)
        return
    # Multiply the current n with the global fact variable
    fact = fact * n
    # Recursive call with n-1
    find_factorial(n - 1)

# Call the function to find factorial of 5
find_factorial(5)

# https://takeuforward.org/pattern/pattern-19-symmetric-void-pattern
# Function to print a symmetric void pattern (hollow diamond-like)
def pattern19(n):
    # Upper half
    for i in range(n, 0, -1):
        print(i * "*", end="")  # Left stars
        print((2 * n - i * 2) * " ", end="")  # Spaces
        print(i * "*", end="")  # Right stars
        print()
    # Lower half
    for i in range(1, n + 1):
        print(i * "*", end="")  # Left stars
        print((2 * n - i * 2) * " ", end="")  # Spaces
        print(i * "*", end="")  # Right stars
        print()

# Call the function with n=30
pattern19(30)
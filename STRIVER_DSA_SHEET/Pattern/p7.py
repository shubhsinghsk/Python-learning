# https://takeuforward.org/pattern/pattern-7-star-pyramid
# Function to print a star pyramid (centered triangle)
def pattern_7(n):
    # Loop for each row
    for i in range(0, n):
        # Print spaces for centering: n-i-1 spaces
        print((n - i - 1) * " " + (2 * i + 1) * "*" + (n - i - 1) * " ")
        # Extra print() for spacing, but it's unnecessary
        print()

# Call the function with n=5
pattern_7(5)
# https://takeuforward.org/pattern/pattern-12-number-crown-pattern
# Function to print a number crown pattern
def pattern12(n):
    # Loop for each row
    for i in range(1, n + 1):
        # Left side: numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end="")
        # Spaces: 2*(n-i) spaces
        print(" " * (2 * (n - i)), end="")
        # Right side: numbers from i down to 1
        for j in range(i, 0, -1):
            print(j, end="")
        # Move to next line
        print()

# Call the function with n=6
pattern12(6)
# https://takeuforward.org/pattern/pattern-14-increasing-letter-triangle-pattern
# Function to print an increasing letter triangle (A, B, C, ...)
def pattern14(n):
    # Loop for each row
    for i in range(1, n + 1):
        # Inner loop for each position in row
        for j in range(i):
            # Print letter: A + j
            print(chr(ord('A') + j), end=" ")
        # Move to next line
        print()

# Call the function with n=5
pattern14(5)
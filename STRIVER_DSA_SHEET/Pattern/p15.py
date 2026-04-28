# https://takeuforward.org/pattern/pattern-15-reverse-letter-triangle-pattern
# Function to print a reverse letter triangle
def pattern15(n):
    # Loop from n down to 1 for rows
    for i in range(n, 0, -1):
        # Inner loop for each position in row
        for j in range(0, i):
            # Print letter: A + j
            print(chr(ord('A') + j), end=" ")
        # Move to next line
        print()

# Call the function with n=7
pattern15(7)
# https://takeuforward.org/pattern/pattern-13-increasing-number-triangle-pattern
# Function to print an increasing number triangle
def pattern13(n):
    c = 1  # Counter for numbers
    # Loop for each row
    for i in range(n):
        # Inner loop for each position in row
        for j in range(i + 1):
            print(c, end=" ")  # Print current counter
            c = c + 1  # Increment counter
        # Move to next line
        print()

# Call the function with n=5
pattern13(5)
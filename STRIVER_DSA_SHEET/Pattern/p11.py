# https://takeuforward.org/pattern/pattern-11-binary-number-triangle-pattern
# Function to print a binary number triangle pattern
def pattern11(n):
    # Loop for each row
    for i in range(n):
        # Inner loop for each position in row
        for j in range(0, i + 1):
            # If (i+j) is even, print 1; else 0
            if (i + j) % 2 == 0:
                print(1, end="")
            if (i + j) % 2 == 1:
                print(0, end="")
        # Move to next line
        print()

# Call the function with n=150 (large for pattern)
pattern11(150)
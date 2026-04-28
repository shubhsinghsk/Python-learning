# https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern
# Function to print an alpha ramp pattern (same letter per row)
def pattern16(n):
    # Loop for each row
    for i in range(n):
        # Inner loop for each position in row
        for j in range(i + 1):
            # Print the letter for the row: A + i
            print(chr(ord('A') + i), end=" ")
        # Move to next line
        print()

# Call the function with n=5
pattern16(5)
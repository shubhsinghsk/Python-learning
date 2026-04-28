# https://takeuforward.org/pattern/pattern-1-rectangular-star-pattern
# Function to print a rectangular star pattern of size n x n
def print_pattern_1(n):
    # Outer loop for each row
    for i in range(n):
        # Inner loop for each column in the row
        for j in range(n):
            print("*", end="")
        # Move to next line after each row
        print("")

# Call the function with n=4
print_pattern_1(4)
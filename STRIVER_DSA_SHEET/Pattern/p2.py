# https://takeuforward.org/pattern/pattern-2-right-angled-triangle-pattern
# Function to print a right-angled triangle pattern of stars
def pattern_2(n):
    # Loop for each row
    for i in range(1, n + 1):
        # Print i stars in each row
        while i > 0:
            print("*", end="")
            i = i - 1  # Decrement i to control the number of stars
        # Move to next line
        print()

# Call the function with n=3
pattern_2(3)
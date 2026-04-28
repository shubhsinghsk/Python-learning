# https://takeuforward.org/pattern/pattern-3-right-angled-number-pyramid
# Function to print a right-angled number pyramid
def pattern_3(n):
    # Loop for each row
    for i in range(1, n + 1):
        # Inner loop to print numbers 1 to i in each row
        for j in range(1, i + 1):
            print(j, end=" ")
        # Move to next line
        print()

# Call the function with n=5
pattern_3(5)
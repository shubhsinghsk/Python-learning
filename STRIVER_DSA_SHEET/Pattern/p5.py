# https://takeuforward.org/pattern/pattern-5-inverted-right-pyramid
# Function to print an inverted right-angled triangle of stars
def pattern_5(n):
    # Loop from n down to 1 for rows
    for i in range(n, 0, -1):
        # Inner loop to print i stars in each row
        for j in range(1, i + 1):
            print("*", end=" ")
        # Move to next line
        print()

# Call the function with n=5
pattern_5(5)

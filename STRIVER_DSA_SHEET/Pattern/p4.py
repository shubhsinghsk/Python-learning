# https://takeuforward.org/pattern/pattern-4-right-angled-number-pyramid-ii
# Function to print a right-angled number pyramid where each row has the row number repeated
def pattern_4(n):
    # Loop for each row
    for i in range(1, n + 1):
        # Inner loop to print i, i times
        for j in range(1, i + 1):
            print(i, end=" ")
        # Move to next line
        print()

# Call the function with n=5
pattern_4(5)
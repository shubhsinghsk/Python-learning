# https://takeuforward.org/pattern/pattern-8-inverted-star-pyramid
# Function to print an inverted star pyramid
def pattern8(n):
    c = 0  # Counter for spaces
    # Loop from n down to 1
    for i in range(n, 0, -1):
        # Print spaces: increasing with c
        print(int((2 * c) / 2) * " " + (2 * i - 1) * "*" + int((2 * c) / 2) * " ")
        print()  # Extra print
        c = c + 1  # Increment space counter

# Call the function with n=5
pattern8(5)
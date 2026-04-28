# https://takeuforward.org/pattern/pattern-9-diamond-star-pattern
# Function to print a diamond star pattern
def pattern9(n):
    # Upper half: pyramid
    for i in range(0, n):
        print((n - i - 1) * " " + (2 * i + 1) * "*" + (n - i - 1) * " ")
        print()

    c = 0
    # Lower half: inverted pyramid
    for i in range(n, 0, -1):
        print(int((2 * c) / 2) * " " + (2 * i - 1) * "*" + int((2 * c) / 2) * " ")
        print()
        c = c + 1

# Call the function with n=5
pattern9(5)
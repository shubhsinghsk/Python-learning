# https://takeuforward.org/pattern/pattern-10-half-diamond-star-pattern
# Function to print a half diamond star pattern
def pattern10(n):
    # Upper half: increasing stars
    for i in range(1, n):
        print(i * "*" + (n - i) * " ")
    # Lower half: decreasing stars
    for j in range(n - 1, 0, -1):
        print(j * "*" + (n - j) * " ")

# Call the function with n=5
pattern10(5)
# Recursive function to print numbers from 1 to n
def print_1_to_n(n):
    if n == 0:
        # Base case: stop when n reaches 0
        return
    # Recursive call for n-1 first (to print smaller numbers first)
    print_1_to_n(n - 1)
    # Then print current n
    print(n)

# Call the function
print_1_to_n(5)
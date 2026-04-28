
# Recursive function to print numbers from n down to 1
def print_n_to_1(n):
    if n == 0:
        # Base case: stop when n reaches 0
        return
    # Print current n first
    print(n, end=' ')
    # Then recursive call for n-1
    print_n_to_1(n - 1)

# Call the function
print_n_to_1(5)
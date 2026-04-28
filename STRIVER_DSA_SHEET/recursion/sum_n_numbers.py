# Global variable to accumulate the sum
sum = 0

# Recursive function to calculate sum of first n natural numbers
def sum_n_numbers(n):
    global sum
    if n == 0:
        # Base case: print the sum when n is 0
        print(sum)
        return
    # Add current n to sum
    sum += n
    # Recursive call for n-1
    sum_n_numbers(n - 1)

# Call the function
sum_n_numbers(5)
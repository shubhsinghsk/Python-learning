# Global counter to track how many times we've printed
count = 0

# Recursive function to print name n times
def print_name_n_time(n):
    global count
    if count == n:
        # Base case: stop when count reaches n
        return
    # Print the name
    print("SHubham")
    # Increment count
    count += 1
    # Recursive call
    print_name_n_time(n)

# Call the function
print_name_n_time(3)
def find_gcd(a, b):
    """
    Find the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        The GCD of a and b
    """
    # Continue the loop until one of the numbers becomes 0
    while a > 0 and b > 0:
        # If a is greater than b, replace a with remainder of a divided by b
        if a > b:
            a = a % b
        # Otherwise, replace b with remainder of b divided by a
        else:
            b = b % a
    
    # Return whichever number is not zero (the GCD)
    # If a is 0, return b; otherwise return a
    return a if a != 0 else b


# Test the function with sample values
print(find_gcd(48, 18))  # Output: 6
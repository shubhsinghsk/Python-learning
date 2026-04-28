def find_armstrong(n):
    """
    Check if a number is an Armstrong number.
    
    An Armstrong number is a number that is equal to the sum of its own digits 
    each raised to the power of the number of digits.
    
    Args:
        n: The number to check
    """
    a = n
    l = 0  # digit count
    sum_val = 0  # sum of powered digits
    l_num = []  # list of digits
    while a != 0:
        l += 1  # increment digit count
        b = a % 10  # extract last digit
        l_num.append(b)
        a = a // 10  # remove last digit
        
    for i in l_num:
        sum_val += pow(i, l)  # add digit^l to sum
    
    return sum_val == n  # return True if Armstrong number
    

"""
SHere are some suggestions for improvement based on AI’s suggestions:

1. Naming Conventions and Readability: In Python, variable names like ‘l’, ‘a’, and ‘b’ are cryptic. Use descriptive names like ‘temp_n’, ‘digit_count’, or ‘digit’ in live interviews. Avoid using ‘sum’ as a variable name, as it’s a built-in function and shadowing it can cause bugs.

2. Space Complexity: Storing every digit in a list (e.g., ‘l_num’) is unnecessary memory usage. Calculate the sum on the fly as you extract digits.

3. Pythonic Shortcuts: Python offers powerful built-ins. For example, ’n // 10’ and ’n % 10’ is a classic approach, but converting the number to a string is often faster to write and easier to read in interviews (unless the interviewer specifically forbids string conversion).

4. Booleans: Instead of:

```python
if sum == n:
return True
else:
return False
```

Simply use:

```python
return sum == n
```
💡 Interviewer’s Pro-Tips:
                                                - Type hinting (e.g., int -> bool) shows familiarity with modern Python (3.5+) and care for code maintainability.
                                                - While pow(x, y) is a built-in function, x ** y is generally preferred for simple exponentiation in Python as it’s more readable.
                                                - Always mention edge cases, such as handling negative or non-integer inputs.
"""

# Here’s how a top-tier candidate might write this:


def is_armstrong(n: int) -> bool:
    # Handle negative numbers (Armstrong numbers are typically natural numbers)
    if n < 0:
        return False

            # Optimisation: Use string conversion for digit count and iteration
    str_n = str(n)
    power = len(str_n)
            
    # Use a generator expression with sum() for O(1) extra space
    total = sum(int(digit) ** power for digit in str_n)
            
    return total == n
                                                
                                                

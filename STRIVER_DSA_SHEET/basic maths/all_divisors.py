# Function to find all divisors of n (brute force approach)
def divisors(n):
    result = []
    if n == 1:
        result.append(1)
    result.append(1)  # Always include 1
    for i in range(2, 11):  # Loop up to 10, but should be up to n
        if n % i == 0:
            temp = n // i
            if i not in result:
                result.append(i)
            if temp not in result:
                result.append(temp)
    if n not in result:
        result.append(n)
    return sorted(result)

print(divisors(100))

# Optimized function using square root
def divisors(n):
    res = set()  # Use set to avoid duplicates
    # Loop from 1 to sqrt(n)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)       # Add the divisor
            res.add(n // i)  # Add the corresponding pair
    return sorted(list(res))
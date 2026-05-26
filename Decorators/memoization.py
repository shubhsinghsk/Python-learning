# Memoization decorator
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            print(f"Computing result for {func.__name__}{args} and caching it.")
            cache[args] = func(*args)
        else:
            print(f"Using cached result for {func.__name__}{args}.")
        return cache[args]

    return wrapper

# Function to be memoized
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Using the memoized function
result1 = fibonacci(5)
result2 = fibonacci(8)
result3 = fibonacci(5)
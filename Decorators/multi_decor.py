# First decorator
def decorator1(func):
    def wrapper():
        print("Decorator 1 - Before function is called.")
        func()
        print("Decorator 1 - After function is called.")
    return wrapper

# Second decorator
def decorator2(func):
    def wrapper():
        print("Decorator 2 - Before function is called.")
        func()
        print("Decorator 2 - After function is called.")
    return wrapper

# Applying multiple decorators
# @decorator1
# @decorator2
def my_function():
    print("Original function.")

# Using the decorated function
# my_function()
result = decorator1(decorator2(my_function)) # 
result()

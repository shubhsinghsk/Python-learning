import functools

#decorator without functool
def decorators1(func):
    def wrapper():
        """Wrapper of decor 1"""
        print(f"calling {func.__name__}")
        func()
    return wrapper

#decorator with functool
def decorators2(func):
    @functools.wraps(func)
    def wrapper():
        """ Wrapper of decor 2"""
        print(f"calling {func.__name__}")
        func()
    return wrapper

@decorators1
def func1():
    """ Original function 1 without wraps"""
    print("func1")

@decorators2
def func2():
    """ Original function 2 with wraps"""
    print("func2")


print(func1.__doc__)
print(func2.__doc__)
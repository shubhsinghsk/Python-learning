def decorators(func):
    def wrapper(a,b):
        print("FUnction execution started")
        result = func(a,b)
        print("Function excution ended")
        return result

    return wrapper

# @decorators
def add(a, b):
    sum = a + b

    return sum

# print(add(1,2))
result = decorators(add)
print(result(1,3))
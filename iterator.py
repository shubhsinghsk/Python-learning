# Demonstrate usage of iterators in Python
l = [10, 20, 30]

# Create an iterator from the list
l_iter = iter(l)
print(f"Type of iterator: {type(l_iter)}")
try:
    # Get next elements from the iterator
    print(next(l_iter))
    print(next(l_iter))
    print(next(l_iter))
    # Uncommenting the next line would raise StopIteration
    # print(next(l_iter))
except StopIteration:
    # Handle when iterator is exhausted
    print("Reached the end of the iterator.")
else:
    # If no exception occurred
    print("All good") 

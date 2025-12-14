l= [10,20,30]

l_iter = iter(l)
print(f"Type of iterator: {type(l_iter)}")
try:
    print(next(l_iter))
    print(next(l_iter))
    print(next(l_iter))
    # print(next(l_iter))
 # This will raise StopIteration
except StopIteration:
    print("Reached the end of the iterator.")
else:
    print("All good") 

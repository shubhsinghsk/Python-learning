# Simple example of inheritance in Python
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    # Bus inherits from Vehicle without adding new methods
    pass

# Create a Bus object
obj1 = Bus('Volve', 10, 20)

# Access inherited attributes
print(obj1.max_speed, obj1.mileage)

        




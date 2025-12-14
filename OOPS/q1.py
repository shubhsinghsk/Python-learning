class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

obj1 = Bus('Volve', 10,20)

print(obj1.max_speed, obj1.mileage)

        




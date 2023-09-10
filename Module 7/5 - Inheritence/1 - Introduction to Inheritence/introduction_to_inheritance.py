# Introduction to Inheritance in Python

# Base (Parent) Class: Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        return f"Accelerating! Current speed is {self.speed} km/h."

    def brake(self):
        self.speed = max(0, self.speed - 10)
        return f"Braking! Current speed is {self.speed} km/h."

    def details(self):
        return f"This is a {self.brand} {self.model}."

# Derived (Child) Class: Car
class Car(Vehicle):
    # For now, we're just using the inherited properties and methods of the Vehicle class.
    # Later, we'll explore adding unique attributes and methods to this child class.
    pass


if __name__ == "__main__":
    # Creating an instance of the Base class
    generic_vehicle = Vehicle("GenericBrand", "GenericModel")
    print(generic_vehicle.details())
    print(generic_vehicle.accelerate())

    # Creating an instance of the Derived class
    my_car = Car("Toyota", "Corolla")
    print(my_car.details())
    print(my_car.accelerate())
    print(my_car.brake())


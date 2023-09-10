# MODULE 7: SECTION 6.2 - Private Attributes and Methods

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._odometer_reading = 0  # Single underscore - conventionally private
        self.__engine_code = "AB123XYZ"  # Double underscores - name mangling to make it harder to access

    # Public method to get the odometer reading
    def read_odometer(self):
        return self._odometer_reading

    # Private method (by convention) to set odometer reading
    def _set_odometer(self, mileage):
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    # Public method to get engine code (showing the principle of encapsulation)
    def get_engine_code(self):
        return self.__reveal_engine_code()

    # Truly private method using double underscores
    def __reveal_engine_code(self):
        return self.__engine_code


# Usage:

my_car = Car("Toyota", "Camry", 2022)

# Accessing conventionally private attribute:
print(my_car.read_odometer())  # Expected output: 0

# Accessing conventionally private method:
# my_car._set_odometer(500)  # Not recommended but possible
# print(my_car.read_odometer())  # Expected output: 500

# Trying to access truly private attribute (This will throw an error):
# print(my_car.__engine_code)  # AttributeError

# Accessing it through a public method:
print(my_car.get_engine_code())  # Expected output: AB123XYZ

# Demonstrating the edge case of still accessing a "private" attribute:
print(my_car._Car__engine_code)  # Expected output: AB123XYZ, but not recommended.


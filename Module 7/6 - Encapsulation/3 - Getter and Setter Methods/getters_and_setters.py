# Module 7 - Section 6.3: Getter and Setter Methods

class Product:
    def __init__(self, name, price):
        self._name = name  # Using underscore signifies it's meant to be private
        self.set_price(price)  # using setter during initialization

    # Getter for name attribute
    def get_name(self):
        return self._name

    # Getter for price attribute
    def get_price(self):
        return self._price

    # Setter for price attribute
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def display(self):
        print(f"Product Name: {self.get_name()}\nProduct Price: ${self.get_price():.2f}")


# Demonstration
try:
    # Creating an instance of the Product class
    item = Product("Laptop", 1000)

    # Displaying product details
    item.display()

    # Attempting to set a negative price using setter - will raise an error
    item.set_price(-500)
except ValueError as e:
    print(f"Error: {e}")

# Changing product price using setter
item.set_price(1200)

# Displaying updated product details
item.display()


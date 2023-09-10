# MODULE 7 - OOP in Python
# Section 3.3 - Class Variables

class Employee:
    """Class to represent an Employee"""

    # Class variable
    # Company name is assumed to be the same for all employees
    company_name = "TechCorp Inc."

    def __init__(self, name, employee_id):
        # Instance variables
        self.name = name
        self.employee_id = employee_id

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Company Name: {Employee.company_name}\n")


class Product:
    """Class to represent a Product in a store"""

    # Class variable for Value Added Tax (VAT) rate
    # VAT is a consumption tax placed on a product whenever value is added at each stage of the supply chain, 
    # from production to the point of sale. Here, we assume a constant VAT rate for all products.
    VAT_rate = 0.15

    def __init__(self, product_name, base_price):
        self.product_name = product_name
        self.base_price = base_price

    def total_price(self):
        """Calculate total price after including VAT"""
        return self.base_price * (1 + Product.VAT_rate)

    def display(self):
        print(f"Product Name: {self.product_name}")
        print(f"Base Price: ${self.base_price}")
        print(f"Total Price after {Product.VAT_rate*100}% VAT: ${self.total_price()}\n")


class Library:
    """Class to represent a Library System"""

    # Class variable
    # The library name is assumed to be the same for all books in this context
    library_name = "Central Library"

    def __init__(self, book_title):
        self.book_title = book_title

    def display(self):
        print(f"Book Title: {self.book_title}")
        print(f"Library Name: {Library.library_name}\n")


if __name__ == "__main__":
    # Create an employee object
    emp1 = Employee("John Doe", "E12345")
    emp1.display()

    # Create a product object
    prod1 = Product("Laptop", 1000)
    prod2 = Product("Mouse", 50)
    prod1.display()
    prod2.display()

    # Create a library object
    book1 = Library("Python Basics")
    book1.display()

    # Updating the class variable through the class itself
    # This will reflect across all instances
    Employee.company_name = "TechCorp Solutions"
    emp2 = Employee("Jane Smith", "E67890")
    emp2.display()

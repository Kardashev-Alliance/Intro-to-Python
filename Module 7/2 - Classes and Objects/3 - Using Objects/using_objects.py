# Class definitions

# Example 1: Object Attribute Manipulation
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def display_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

# Create a Book object
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
print(book1.display_info())

# Modifying attributes of the book object
book1.title = "The Great Gatsby: Special Edition"
print(book1.display_info())

# Example 2: Objects as Function Parameters
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        return f"{self.name}, {self.age} years old."

def greet(person_obj):
    return f"Hello, {person_obj.name}!"

# Using Person object as a function parameter
person1 = Person("Alice", 25)
print(greet(person1))

# Example 3: Interacting Objects
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def spend(self, cost):
        if self.amount >= cost:
            self.amount -= cost
            return True
        else:
            return False

class Store:
    def __init__(self, item, stock, price):
        self.item = item
        self.stock = stock
        self.price = price

    def purchase(self, wallet_obj):
        if wallet_obj.spend(self.price) and self.stock > 0:
            self.stock -= 1
            return f"Purchased {self.item}."
        elif self.stock == 0:
            return f"{self.item} is out of stock."
        else:
            return f"Not enough funds to purchase {self.item}."

# Interacting Wallet and Store objects
wallet1 = Wallet(50)  # $50 in the wallet
store1 = Store("Laptop", 10, 45)  # 10 laptops at $45 each

print(store1.purchase(wallet1))  # should reduce the amount in the wallet and decrease the store stock


# Module 7, Section 3.2: Instance Variables

# ----- Example 1: Personal Profile -----

class Person:
    # The __init__ method initializes the instance variables for each object.
    def __init__(self, name, age, address):
        self.name = name        # 'name' instance variable
        self.age = age          # 'age' instance variable
        self.address = address  # 'address' instance variable

    # This method displays the details of the person.
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Creating two different objects of the Person class.
person1 = Person("John Doe", 25, "123 Main St")
person2 = Person("Jane Smith", 30, "456 Elm St")

# As you can see, both objects have their own unique data.
person1.display()  # Output: Name: John Doe, Age: 25, Address: 123 Main St
person2.display()  # Output: Name: Jane Smith, Age: 30, Address: 456 Elm St


# ----- Example 2: Bank Account -----

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # 'account_number' instance variable
        self.balance = balance                # 'balance' instance variable

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")

# Creating two bank account objects.
account1 = BankAccount("00123", 500)
account2 = BankAccount("00124", 1000)

account1.display_balance()  # Output: Account Number: 00123, Balance: $500
account2.display_balance()  # Output: Account Number: 00124, Balance: $1000


# ----- Example 3: Book Library -----

class Book:
    def __init__(self, title, author, isbn):
        self.title = title     # 'title' instance variable
        self.author = author   # 'author' instance variable
        self.isbn = isbn       # 'isbn' instance variable

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

# Creating two book objects.
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("Moby Dick", "Herman Melville", "9781503280786")

book1.display()  # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 9780743273565
book2.display()  # Output: Title: Moby Dick, Author: Herman Melville, ISBN: 9781503280786

# SUMMARY:
# As shown in the above examples, instance variables are pivotal in defining the state of each object.
# Each object has its own set of instance variables, thereby preserving its unique identity.

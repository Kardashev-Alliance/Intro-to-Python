# CLI Contact Book
# Module 8: Section 2.3 - Building the CLI Contact Book

'''
SQLite3 in Python: Key Methods Overview

The sqlite3 module in Python provides an interface to the SQLite database. 
SQLite is a C library that provides a lightweight, serverless, self-contained, high-reliability, full-featured SQL database engine. 
Below is a rundown of some of the core methods used when interacting with SQLite databases using the sqlite3 module in Python:

1. sqlite3.connect(database_name):
   - Purpose: This method is used to establish a connection to an SQLite database. 
   - Parameters:
     - database_name: Name of the SQLite database. If the database does not exist, a new one is created.
   - Returns: A connection object that represents the database.

     Example:
     ```
     conn = sqlite3.connect('example.db')
     ```

2. conn.cursor():
   - Purpose: This method is used to create a cursor object. The cursor is essential for executing SQL queries and fetching results.
   - Returns: A new cursor object using the connection.

     Example:
     ```
     cursor = conn.cursor()
     ```

3. cursor.execute(sql_command):
   - Purpose: Executes an SQL command.
   - Parameters:
     - sql_command: The SQL command to be executed.
   - Note: Use '?' as a placeholder for query parameters to prevent SQL injection attacks.

     Example:
     ```
     cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
     ```

4. conn.commit():
   - Purpose: Commits the current transaction. If you don’t call this method, anything you did since the last call to commit() is not visible to other database connections.
   - Note: It's essential to commit your changes if you're making modifications to the database (INSERT, UPDATE, DELETE).

     Example:
     ```
     conn.commit()
     ```

5. cursor.fetchall():
   - Purpose: Fetches all rows from the result of the last executed SQL command.
   - Returns: A list of tuples where each tuple represents a row.

     Example:
     ```
     cursor.execute("SELECT * FROM users")
     all_rows = cursor.fetchall()
     ```

6. conn.close():
   - Purpose: Closes the database connection. It's a best practice to close the connection once you're done with your operations.

     Example:
     ```
     conn.close()
     ```

It's important to handle exceptions and ensure that resources like connections and cursors are properly closed after use. 
Using the 'with' statement can help in automatically committing or rolling back transactions and closing the connection.
'''

import sqlite3

# Database initialization for persistent storage
conn = sqlite3.connect('contact_book.db')
cursor = conn.cursor()

# Create the table if it doesn't exist.
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()

# Data Structures

# Contact representation
def create_contact(name, phone, email):
    """Return a dictionary representing a contact."""
    return {'name': name, 'phone': phone, 'email': email}

# List to hold our contacts - though we'll move more to the database as we evolve the code.
contacts_list = []

# Modules & Interfaces

# Data Management Module

def add_contact(contact):
    """Add a new contact to the database."""
    cursor.execute('''
    INSERT INTO contacts (name, phone, email)
    VALUES (?, ?, ?)
    ''', (contact['name'], contact['phone'], contact['email']))
    conn.commit()

def edit_contact(id, contact):
    """Edit an existing contact."""
    cursor.execute('''
    UPDATE contacts
    SET name = ?, phone = ?, email = ?
    WHERE id = ?
    ''', (contact['name'], contact['phone'], contact['email'], id))
    conn.commit()

def delete_contact(id):
    """Delete a contact using its ID."""
    cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()

def list_contacts():
    """List all contacts."""
    cursor.execute('SELECT id, name, phone, email FROM contacts')
    return cursor.fetchall()

# Search Module

def search_contact(attribute, value):
    """Search for a contact based on an attribute."""
    cursor.execute(f'SELECT id, name, phone, email FROM contacts WHERE {attribute} = ?', (value,))
    return cursor.fetchall()

# Backup & Restore Module

# For this version, we'll assume backup and restore are placeholders, but they could be expanded to save to and load from external files or cloud storage.
def backup_data():
    """Backup contact data."""
    print("Backup successful. Data is stored in the local database.")

def restore_data():
    """Restore contact data."""
    print("Data is restored from the local database.")

# CLI Module

def main_cli():
    """Main CLI function."""
    while True:
        print("\nOptions:")
        print("1: Add Contact")
        print("2: Edit Contact")
        print("3: Delete Contact")
        print("4: List Contacts")
        print("5: Search Contacts")
        print("6: Backup Data")
        print("7: Restore Data")
        print("8: Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = create_contact(name, phone, email)
            add_contact(contact)
            print(f"Added contact: {name}")

        elif choice == '2':
            id = int(input("Enter contact ID to edit: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contact = create_contact(name, phone, email)
            edit_contact(id, contact)
            print(f"Edited contact with ID: {id}")

        elif choice == '3':
            id = int(input("Enter contact ID to delete: "))
            delete_contact(id)
            print(f"Deleted contact with ID: {id}")

        elif choice == '4':
            print("\nContacts:")
            for contact in list_contacts():
                print(f"ID: {contact[0]} - Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")

        elif choice == '5':
            attribute = input("Search by (name/phone/email): ")
            value = input("Enter the search value: ")
            results = search_contact(attribute, value)
            if results:
                print(f"\nFound {len(results)} results:")
                for contact in results:
                    print(f"ID: {contact[0]} - Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
            else:
                print("No contacts found for the search criteria.")

        elif choice == '6':
            backup_data()

        elif choice == '7':
            restore_data()

        elif choice == '8':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main_cli()

# Remember to close the database connection when done
conn.close()

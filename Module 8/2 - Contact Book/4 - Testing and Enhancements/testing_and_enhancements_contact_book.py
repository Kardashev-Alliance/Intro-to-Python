# Module 8: Section 2.4 - Testing and Enhancements for the CLI Contact Book

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
import unittest

# Database initialization for persistent storage
conn = sqlite3.connect('contact_book_test.db')
cursor = conn.cursor()

# Create the table if it doesn't exist.
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    group_name TEXT
)
''')

conn.commit()

# Data Structures

def create_contact(name, phone, email, group_name=None):
    """Return a dictionary representing a contact."""
    return {'name': name, 'phone': phone, 'email': email, 'group_name': group_name}

# Modules & Interfaces

# Data Management Module

def add_contact(contact):
    """Add a new contact to the database."""
    cursor.execute('''
    INSERT INTO contacts (name, phone, email, group_name)
    VALUES (?, ?, ?, ?)
    ''', (contact['name'], contact['phone'], contact['email'], contact['group_name']))
    conn.commit()

def edit_contact(id, contact):
    """Edit an existing contact."""
    cursor.execute('''
    UPDATE contacts
    SET name = ?, phone = ?, email = ?, group_name = ?
    WHERE id = ?
    ''', (contact['name'], contact['phone'], contact['email'], contact['group_name'], id))
    conn.commit()

def list_contacts():
    """List all contacts."""
    cursor.execute('SELECT id, name, phone, email, group_name FROM contacts')
    return cursor.fetchall()

# Search Module

def search_contact(attribute, value):
    """Search for a contact based on an attribute."""
    cursor.execute(f'SELECT id, name, phone, email, group_name FROM contacts WHERE {attribute} = ?', (value,))
    return cursor.fetchall()

# CLI Module

# Here, we're focusing on testing and enhancements, so the full CLI won't be reiterated.

# Enhancements

def assign_group(id, group_name):
    """Assign a contact to a group."""
    cursor.execute('''
    UPDATE contacts
    SET group_name = ?
    WHERE id = ?
    ''', (group_name, id))
    conn.commit()

def list_group_contacts(group_name):
    """List contacts based on their group."""
    cursor.execute('SELECT id, name, phone, email FROM contacts WHERE group_name = ?', (group_name,))
    return cursor.fetchall()

# Testing

class TestContactBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Creating some mock contacts
        cls.contact1 = create_contact("John Doe", "+1234567890", "john@example.com", "Friends")
        cls.contact2 = create_contact("Jane Smith", "+0987654321", "jane@example.com", "Family")

    def test_add_and_list_contacts(self):
        add_contact(self.contact1)
        add_contact(self.contact2)
        contacts = list_contacts()
        self.assertIn(("John Doe", "+1234567890", "john@example.com", "Friends"), contacts)
        self.assertIn(("Jane Smith", "+0987654321", "jane@example.com", "Family"), contacts)

    def test_search_contact(self):
        results = search_contact('name', 'John Doe')
        self.assertIn(("John Doe", "+1234567890", "john@example.com", "Friends"), results)

    def test_assign_and_list_group(self):
        contact_id = search_contact('name', 'Jane Smith')[0][0]
        assign_group(contact_id, "Colleagues")
        results = list_group_contacts("Colleagues")
        self.assertIn(("Jane Smith", "+0987654321", "jane@example.com", "Colleagues"), results)

    @classmethod
    def tearDownClass(cls):
        # Clean up (remove test data) after tests are done.
        cursor.execute('DELETE FROM contacts')
        conn.commit()

if __name__ == '__main__':

     # 1. Add contacts
    john = create_contact("John Doe", "+1234567890", "john@example.com", "Friends")
    jane = create_contact("Jane Smith", "+0987654321", "jane@example.com", "Family")
    add_contact(john)
    add_contact(jane)

    # 2. List contacts
    print("Contacts after adding John and Jane:")
    for contact in list_contacts():
        print(contact)

    # 3. Search by name
    print("\nSearching for John Doe:")
    for contact in search_contact('name', 'John Doe'):
        print(contact)

    # 4. Assign a group to Jane
    jane_id = search_contact('name', 'Jane Smith')[0][0]
    assign_group(jane_id, "Colleagues")

    # 5. List contacts in the 'Colleagues' group
    print("\nContacts in 'Colleagues' group:")
    for contact in list_group_contacts("Colleagues"):
        print(contact)

    # 6. Edit Jane's details
    edited_jane = create_contact("Jane Smith", "+0987654321", "jane@newdomain.com", "Colleagues")
    edit_contact(jane_id, edited_jane)
    print("\nJane's details after editing:")
    for contact in search_contact('name', 'Jane Smith'):
        print(contact)



    unittest.main()

# Remember to close the database connection when done
conn.close()

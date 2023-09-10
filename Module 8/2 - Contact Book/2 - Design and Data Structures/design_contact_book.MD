# Module 8: Section 2.2 - Design and Data Structures for the CLI Contact Book

---

## 1. Introduction

This section delves into the design and data structure considerations for the CLI Contact Book project. Being a CLI-based application, we emphasize simplicity, performance, and ease of use. We'll explore the design of the user interface, data structures for contact storage, and the communication between different modules.

---

## 2. Design Principles

### 2.1 User-Centered

- The CLI design aims to be intuitive, even for users unfamiliar with command-line tools.
  
### 2.2 Modularity

- Distinct functionalities are encapsulated in separate modules to ensure code maintainability and clarity.

### 2.3 Scalability

- The design allows for future feature additions, modifications, and enhancements.

---

## 3. Data Structures

### 3.1 Contact Data

- Each contact is represented as a **dictionary** with keys being attributes like name, phone, email, etc.
  
### 3.2 Contact List

- A **list** of contact dictionaries representing the entire contact book.

### 3.3 Persistent Storage

- SQLite database tables for storing contact data, ensuring data consistency, durability, and efficient search.

---

## 4. Modules & Interfaces

### 4.1 CLI Module

- **Purpose:** Capture user commands and display results or messages.
- **Interface:** Text prompts and input fields, command options, and feedback messages.

### 4.2 Data Management Module

- **Purpose:** CRUD operations for contacts.
- **Interface:** Functions like `add_contact()`, `edit_contact()`, `delete_contact()`, and `list_contacts()`.

### 4.3 Search Module

- **Purpose:** Locate contacts based on attributes.
- **Interface:** Function such as `search_contact(attribute, value)`.

### 4.4 Backup & Restore Module

- **Purpose:** Save and load contact data.
- **Interface:** Functions like `backup_data()` and `restore_data()`.

---

## 5. Module Communication

Modules communicate via function calls:

- **CLI -> Data Management:** User's CRUD commands result in respective function calls.
- **CLI -> Search Module:** User's search requests trigger the search function with appropriate attributes.
- **CLI -> Backup & Restore:** User's save/load commands call respective backup or restore functions.
  
Error handling mechanisms ensure that user inputs are validated before processing and that errors are communicated back to the user in a comprehensible manner.

---

## 6. Important Design Decisions

### 6.1 Data Validation

- Data entered by users (e.g., phone numbers, emails) are validated for format and correctness.

### 6.2 Error Feedback

- Display meaningful error messages instead of raw exceptions or errors, guiding the user to rectify their inputs.

### 6.3 Command Design

- Prioritize intuitive and straightforward command names to improve user experience.

---

## 7. Tips for New Developers

1. **Code Readability:** Prioritize writing readable code with meaningful variable and function names.
2. **Function Documentation:** Comment functions to explain their purpose, inputs, and expected outputs.
3. **Iterative Development:** Implement and test in small chunks for efficient bug identification and fixing.
4. **Data Integrity:** Ensure that CRUD operations maintain the integrity of the contact data.

---

## 8. Conclusion

Building the CLI Contact Book requires understanding the design, data structures, module communication, and user interactions. This foundational knowledge ensures a smooth development process and an effective, user-friendly final product.

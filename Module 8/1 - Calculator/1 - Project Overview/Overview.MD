## Calculator Project: Design Document

---

### 1. Overview

The goal of this project is to create a calculator that performs basic arithmetic operations. The calculator will be both user-friendly and versatile, allowing for both command-line operations and potential future integration with a graphical interface.

---

### 2. Core Features

- **Basic Arithmetic Operations:** Add, Subtract, Multiply, Divide.
- **Advanced Operations (stretch goals):** Square root, Power, Sin, Cos, Tan.
- **History:** Ability to view past calculations.

---

### 3. Interfaces

#### 3.1 User Interface (UI)

- **Command Line Interface (CLI):** Initial implementation will focus on a text-based interface where users input their calculations and receive a result.
  
#### 3.2 Graphical User Interface (GUI) [Future Scope]

- Depending on the project's success, a graphical interface may be developed using frameworks like `Tkinter` or `PyQt`.

---

### 4. Architecture

#### 4.1 Modules and Components

- **Main Module:** Drives the application, interfaces with user input and display.
- **Arithmetic Module:** Contains functions for all basic and advanced mathematical operations.
- **History Module:** Manages the storing, retrieving, and clearing of previous calculations.

#### 4.2 Data Flow

1. User provides input via CLI.
2. Main module parses input and identifies the desired operation.
3. The operation is passed to the Arithmetic module.
4. The result is retrieved and displayed to the user.
5. Simultaneously, the input and result are stored in the History module.

---

### 5. Trade-offs and Decisions

#### 5.1 Why CLI initially and not GUI?

- **Development Speed:** CLI can be developed and tested faster.
- **Versatility:** Easier to integrate with other systems or scripts.

#### 5.2 Storing History In-Memory vs. Persistent Storage

- **In-memory** is faster and easier to implement, but history is lost when the application is closed.
- **Persistent storage** would allow history to remain across sessions but requires additional development effort and introduces concerns regarding storage limits and data security.

Decision: Start with in-memory for simplicity, with potential future migration to persistent storage.

#### 5.3 Inclusion of Advanced Operations

- While the core focus is on basic arithmetic, the addition of more advanced operations could make our calculator more versatile and appeal to a broader user base.

Decision: Implement basic operations first and consider advanced operations as stretch goals based on project timeline and feedback.

---

### 6. Future Enhancements

- **Graphical User Interface (GUI):** A more user-friendly interface with buttons for operations.
- **Scientific Operations:** Expanding beyond basic arithmetic to cater to more advanced users.
- **Customizability:** Allowing users to customize the appearance, operation buttons, and more.

---

### 7. Conclusion

This project aims to build a robust calculator application that, while simple in its initial goals, has the architecture and scalability to expand and adapt to more advanced features and interfaces in the future. Proper design and planning will be crucial to ensure the project's longevity and adaptability.

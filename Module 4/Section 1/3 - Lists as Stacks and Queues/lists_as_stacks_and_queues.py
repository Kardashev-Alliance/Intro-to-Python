# ======================================
# Module 4, Section 1.4: Lists as Stacks and Queues
# ======================================

# ============================
# Custom Stack Implementation
# ============================

# Introduction: A stack operates on a "Last In, First Out" (LIFO) structure.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# --- Example 1: Using the custom Stack
stack = Stack()

# Push items onto the stack
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Top of stack after pushes: {stack.peek()}")  # Output: 3

# Pop items from the stack
print(f"Popped from stack: {stack.pop()}")  # Output: 3
print(f"Top of stack after pop: {stack.peek()}")  # Output: 2


# ============================
# Custom Queue Implementation
# ============================

# Introduction: A queue works on a "First In, First Out" (FIFO) principle.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# --- Example 2: Using the custom Queue
queue = Queue()

# Enqueue items
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(f"Front of queue after enqueue operations: {queue.peek()}")  # Output: 'a'

# Dequeue items
print(f"Dequeued from queue: {queue.dequeue()}")  # Output: 'a'
print(f"Front of queue after dequeue: {queue.peek()}")  # Output: 'b'

# ============================
# Conclusion
# ============================

# Custom structures like Stack and Queue can be created to suit specific needs using Python lists.
# They offer clear methods for data manipulations according to the data structure's properties.

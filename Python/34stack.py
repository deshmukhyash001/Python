class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack size:", stack.size())  # Output: 3
print("Top element:", stack.peek())  # Output: 30
print("Popped:", stack.pop())        # Output: 30
print("Stack after popping:", stack.stack)  # Output: [10, 20]
print("Is stack empty?", stack.is_empty())  # Output: False

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"{data} pushed")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(f"{self.stack.pop()} popped")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.peek()

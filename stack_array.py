class StackArray:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.stack)

# Example usage:
stack_array = StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)
print("Stack Array:", stack_array.stack)
print("Pop:", stack_array.pop())
print("Peek:", stack_array.peek())
print("Size:", stack_array.size())

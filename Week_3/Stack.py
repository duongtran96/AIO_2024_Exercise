class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.stack) == self.capacity:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            print("Error")
        self.stack.append(value)

    def top(self):
        if self.is_empty():
            print("Stack is empty")
        return self.stack[-1]

    def __call__(self):
        return self.stack


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1())

print("_____")
print(stack1.pop())
print(stack1())

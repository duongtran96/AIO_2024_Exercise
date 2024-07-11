class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.queue) == self.capacity:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue.append(value)

    def front(self):
        return self.queue[-1]

    def __call__(self):
        return self.queue


queue1 = MyQueue(capacity=4)
queue1.enqueue(2)
print(queue1())
queue1.enqueue(7)
print(queue1())
queue1.enqueue(8)
queue1.enqueue(10)
print("__________")
print(queue1())
queue1.enqueue(11)
queue1.dequeue()
print(queue1())

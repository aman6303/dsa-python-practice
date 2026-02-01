class CircularQueue:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.arr[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"

        removed = self.arr[self.front]
        self.arr[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return removed

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        i = self.front
        while True:
            print(self.arr[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size

class MyDeque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            return "Empty queue"
        print(self.items)

    def enqueue_at_begin(self, value):
        self.items.insert(0, value)
        self.display()

    def enqueue_at_end(self, value):
        self.items.append(value)
        self.display()

    def dequeue_at_end(self):
        if self.is_empty():
            return "Empty queue"
        deleted = self.items.pop()
        self.display()
        return deleted

    def dequeue_at_begin(self):
        if self.is_empty():
            return "Empty queue"

        deleted = self.items.pop(0)
        self.display()
        return deleted

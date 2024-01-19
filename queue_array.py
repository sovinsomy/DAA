class QueueArray:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def size(self):
        return len(self.queue)

# Example usage:
queue_array = QueueArray()
queue_array.enqueue(1)
queue_array.enqueue(2)
queue_array.enqueue(3)
print("Queue Array:", queue_array.queue)
print("Dequeue:", queue_array.dequeue())
print("Size:", queue_array.size())

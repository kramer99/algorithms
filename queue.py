"""
Pretty trivial FIFO
"""
class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, entry):
        self.data.append(entry)

    def dequeue(self):
        return self.data.pop(0)

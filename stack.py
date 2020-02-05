"""
Pretty trivial LIFO
"""
class Stack:

    def __init__(self):
        self.data = []

    def push(self, entry):
        self.data.append(entry)

    def pop(self):
        return self.data.pop()

class Stack(object):
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1:][0]

    def push(self, value):
        self.stack.insert(len(self.stack), value)

    def pop(self):
        value = self.top()
        self.stack = self.stack[:-1]
        return value



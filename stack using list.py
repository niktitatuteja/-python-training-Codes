class stack:
    def __init__(self):
        self.top = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.top) ==0:
            return "Stack is empty"
        return self.top.pop()
    def peek(self):
        if len(self.top) ==0:
            return "Stack is empty"
        return self.top[-1]
    def is_empty(self):
        return not len(self.top) == 0
    def size(self):
        return len(self.top)
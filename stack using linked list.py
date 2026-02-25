class node:
    def __init__(self,data = None):
        self.value=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
        self.length = 0

    def isEmpty(self):
        return self.length == 0
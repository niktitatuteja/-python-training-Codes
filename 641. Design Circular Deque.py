class Node:
    def __init__(self, data=None):
        self.value = data
        self.prev = None
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.f = None
        self.b = None

    def insertFront(self, value: int) -> bool:
        if self.size < self.cap:
            temp = Node(value)

            if self.f is None:
                self.f = self.b = temp
            else:
                temp.next = self.f
                self.f.prev = temp
                self.f = temp

            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.cap:
            temp = Node(value)

            if self.b is None:
                self.f = self.b = temp
            else:
                self.b.next = temp
                temp.prev = self.b
                self.b = temp

            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.f is None:
            return False

        if self.f == self.b:
            self.f = self.b = None
        else:
            self.f = self.f.next
            self.f.prev = None

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.b is None:
            return False

        if self.f == self.b:
            self.f = self.b = None
        else:
            self.b = self.b.prev
            self.b.next = None

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.f is None:
            return -1
        return self.f.value

    def getRear(self) -> int:
        if self.b is None:
            return -1
        return self.b.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
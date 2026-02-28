class Node:
    def __init__(self,data=None):
        self.value=data
        self.next=None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity=k
        self.front=None
        self.back=None
        self.size=0

    def enQueue(self, value: int) -> bool:
        if self.size<self.capacity:
            self.size+=1
            temp=Node(value)
            if self.front==None:
                self.front=self.back=temp
            else:
                self.back.next=temp
                self.back=temp
            return True
        return False

    def deQueue(self) -> bool:
        if self.back==None:
            return False
        if self.back==self.front:
            self.front=self.back=None
        else:
            self.front=self.front.next
        self.size -=1
        return True
    

    def Front(self) -> int:
        if self.front==None:
            return -1
        return self.front.value

    def Rear(self) -> int:
        if self.back==None:
            return -1
        return self.back.value

    def isEmpty(self) -> bool:
        return self.back==None

    def isFull(self) -> bool:
        return self.capacity == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
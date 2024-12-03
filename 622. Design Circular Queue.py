class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k

        self.r = -1
        self.f = -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.f = 0
        
        self.r += 1
        if self.r == self.size:
            self.r = 0
        
        self.queue[self.r] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.f == self.r:
            self.f = -1
            self.r = -1

        else:
            self.f += 1
            if self.f == self.size:
                self.f = 0
        
        return True        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.f]
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.r]
        return -1
        

    def isEmpty(self) -> bool:
        return self.f == -1
        

    def isFull(self) -> bool:
        return (self.r + 1 == self.f) or (self.r + 1 == self.size and self.f == 0)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
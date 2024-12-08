class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

        self.r = -1
        self.f = -1
        

    def pushFront(self, val: int) -> None:
        if self.queue:
            self.queue.insert(0, val)
        else:
            self.queue.append(val)
        

    def pushMiddle(self, val: int) -> None:
        middle_index = len(self.queue) // 2
        self.queue.insert(middle_index, val)
        

    def pushBack(self, val: int) -> None:
        self.queue.insert(len(self.queue), val)
        

    def popFront(self) -> int:
        if self.queue:
            print(self.queue)
            return self.queue.pop(0)
        return -1
        

    def popMiddle(self) -> int:
        if self.queue:
            middle_index = (len(self.queue) - 1) // 2
            return self.queue.pop(middle_index)
        return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
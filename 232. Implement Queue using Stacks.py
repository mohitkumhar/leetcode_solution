class MyQueue:

    def __init__(self):
        self.queue = []
        self.f = 0

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            x = self.queue[self.f]
            self.f += 1
            return x

    def peek(self) -> int:
        if not self.empty():
            return self.queue[self.f]

    def empty(self) -> bool:
        return self.f == len(self.queue)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

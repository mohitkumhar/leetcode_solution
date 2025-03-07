class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1
        

    def increment(self, k: int, val: int) -> None:
        for index in range(min(k, len(self.stack))):
            self.stack[index] = self.stack[index] + val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
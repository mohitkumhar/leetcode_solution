class MyCalendarTwo:
    def __init__(self):
        self.counter = {}

    def book(self, startTime: int, endTime: int) -> bool:
        self.counter[startTime] = self.counter.get(startTime, 0) + 1
        self.counter[endTime] = self.counter.get(endTime, 0) - 1
        count = 0

        for key, values in sorted(self.counter.items()):
            count += values

            if count > 2:
                self.counter[startTime] -= 1
                self.counter[endTime] += 1
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)

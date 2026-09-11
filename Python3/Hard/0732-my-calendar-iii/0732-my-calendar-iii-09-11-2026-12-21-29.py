class MyCalendarThree:

    def __init__(self):
        self.map = {}
        self.result = []

    def book(self, startTime: int, endTime: int) -> int:
        self.map[startTime] = self.map.get(startTime, 0) + 1
        self.map[endTime] = self.map.get(endTime, 0) - 1
        currVal = 0
        maxVal = 0

        for key, values in sorted(self.map.items()):
            currVal += values
            maxVal = max(maxVal, currVal)

        self.result.append(maxVal)

        return maxVal


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

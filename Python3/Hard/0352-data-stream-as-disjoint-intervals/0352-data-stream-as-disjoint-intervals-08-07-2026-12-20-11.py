class SummaryRanges:

    def __init__(self):
        self.summaryRanges = set()

    def addNum(self, value: int) -> None:
        self.summaryRanges.add(value)

    def getIntervals(self) -> List[List[int]]:
        result = []

        nums = list(self.summaryRanges)
        nums.sort()

        n = len(nums)
        i = 0

        while i < n:
            left = nums[i]
            while i < (n - 1) and nums[i] + 1 == nums[i + 1]:
                i += 1

            result.append([left, nums[i]])

            i += 1
        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

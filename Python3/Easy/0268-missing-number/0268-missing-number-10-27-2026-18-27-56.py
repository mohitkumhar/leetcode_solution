class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        expectedSum = (n * (n + 1)) // 2
        actualSum = sum(nums)

        return expectedSum - actualSum

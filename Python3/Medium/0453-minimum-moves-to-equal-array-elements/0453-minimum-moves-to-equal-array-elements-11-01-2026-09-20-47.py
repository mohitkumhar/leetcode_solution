class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minElement = min(nums)
        totalOperation = 0

        for num in nums:
            totalOperation += num - minElement

        return totalOperation

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        totalMove = 0
        maxElement = max(nums)

        for num in nums:
            totalMove += maxElement - num

        return totalMove

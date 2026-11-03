class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        if n % 2 == 1:
            median = nums[n // 2]
        else:
            median = (nums[n // 2] + nums[n // 2 - 1]) // 2

        totalMoves = 0

        for num in nums:
            totalMoves += abs(median - num)
        return totalMoves

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for num in sorted(nums, reverse=True):
            if (-1 * num) in nums:
                return num
        return -1

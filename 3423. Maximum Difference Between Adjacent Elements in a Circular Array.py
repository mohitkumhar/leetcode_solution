class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums)):
            result = max(result, abs(nums[i - 1] - nums[i]))
        
        result = max(result, abs(nums[0] - nums[len(nums) - 1]))
        return result

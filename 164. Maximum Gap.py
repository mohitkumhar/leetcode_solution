class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        result = 0
        for i in range(len(nums) - 1):
            result = max(result, nums[i + 1] - nums[i])

        return result

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        result = [0] * len(nums)

        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            result[i] = max(result[i - 1], nums[i] + result[i - 2])
        
        return result[-1]

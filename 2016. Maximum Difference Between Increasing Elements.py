class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -1
        min1 = nums[0]

        for i in range(1, len(nums)):
            min1 = min(min1, nums[i])
            if min1 < nums[i]:
                result = max(result, nums[i] - min1)

        return result

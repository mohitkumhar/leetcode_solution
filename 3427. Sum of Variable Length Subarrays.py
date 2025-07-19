class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            result += sum(nums[start: i + 1])

        return result

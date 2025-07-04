class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        maximum_value = nums[-1] * nums[-2]
        minimum_value = nums[0] * nums[1]

        return maximum_value - minimum_value

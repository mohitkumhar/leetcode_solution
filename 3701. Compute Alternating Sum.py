class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        addition = 0
        subtraction = 0

        for i in range(0, len(nums), 2):
            addition += nums[i]
        for i in range(1, len(nums), 2):
            subtraction += nums[i]

        return addition - subtraction

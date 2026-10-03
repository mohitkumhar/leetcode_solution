class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total = 0
        current = 0

        for i in range(2, len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                current += 1
                total += current
            else:
                current = 0

        return total

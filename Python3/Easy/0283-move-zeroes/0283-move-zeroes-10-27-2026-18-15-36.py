class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        n = len(nums)

        for j in range(n):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1

        return nums
